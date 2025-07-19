import json
from web3 import Web3

# Настройка подключения к локальному или удалённому Ethereum узлу
w3 = Web3(Web3.HTTPProvider('http://localhost:8545'))

# Контракт ABI (упрощённый пример)
contract_abi = json.loads('''[
    {
        "inputs": [{"internalType": "address","name": "guardian","type": "address"}],
        "name": "addGuardian",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "inputs": [{"internalType": "address","name": "guardian","type": "address"}],
        "name": "removeGuardian",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "inputs": [{"internalType": "address","name": "guardian","type": "address"}],
        "name": "isGuardian",
        "outputs": [{"internalType": "bool","name": "","type": "bool"}],
        "stateMutability": "view",
        "type": "function"
    }
]''')

# Адрес развернутого контракта (пример)
contract_address = Web3.toChecksumAddress('0x1234567890abcdef1234567890abcdef12345678')

contract = w3.eth.contract(address=contract_address, abi=contract_abi)

def check_guardian(address):
    return contract.functions.isGuardian(Web3.toChecksumAddress(address)).call()

def add_guardian(account, private_key, guardian_address):
    nonce = w3.eth.get_transaction_count(account)
    txn = contract.functions.addGuardian(Web3.toChecksumAddress(guardian_address)).build_transaction({
        'from': account,
        'nonce': nonce,
        'gas': 200000,
        'gasPrice': w3.toWei('5', 'gwei')
    })
    signed_txn = w3.eth.account.sign_transaction(txn, private_key=private_key)
    tx_hash = w3.eth.send_raw_transaction(signed_txn.rawTransaction)
    return w3.toHex(tx_hash)

def remove_guardian(account, private_key, guardian_address):
    nonce = w3.eth.get_transaction_count(account)
    txn = contract.functions.removeGuardian(Web3.toChecksumAddress(guardian_address)).build_transaction({
        'from': account,
        'nonce': nonce,
        'gas': 200000,
        'gasPrice': w3.toWei('5', 'gwei')
    })
    signed_txn = w3.eth.account.sign_transaction(txn, private_key=private_key)
    tx_hash = w3.eth.send_raw_transaction(signed_txn.rawTransaction)
    return w3.toHex(tx_hash)

# Пример использования
if __name__ == "__main__":
    account = '0xYourAccountAddress'
    private_key = 'your_private_key_here'
    guardian = '0xGuardianAddressHere'

    print(f"Is guardian? {check_guardian(guardian)}")
    tx_add = add_guardian(account, private_key, guardian)
    print(f"Add guardian TX hash: {tx_add}")
    tx_remove = remove_guardian(account, private_key, guardian)
    print(f"Remove guardian TX hash: {tx_remove}")

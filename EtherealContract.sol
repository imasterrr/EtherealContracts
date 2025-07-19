// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

/// @title Ethereal Unique Contract
/// @notice This contract implements a novel pattern of dynamic permissions
contract EtherealUniqueContract {
    mapping(address => bool) private _etherealGuardians;
    address public immutable creator;

    event GuardianAdded(address guardian);
    event GuardianRemoved(address guardian);

    modifier onlyGuardian() {
        require(_etherealGuardians[msg.sender], "Not an ethereal guardian");
        _;
    }

    constructor() {
        creator = msg.sender;
        _etherealGuardians[creator] = true;
        emit GuardianAdded(creator);
    }

    /// @notice Add a new guardian with dynamic role
    /// @param guardian The address to add
    function addGuardian(address guardian) external onlyGuardian {
        _etherealGuardians[guardian] = true;
        emit GuardianAdded(guardian);
    }

    /// @notice Remove a guardian
    /// @param guardian The address to remove
    function removeGuardian(address guardian) external onlyGuardian {
        require(guardian != creator, "Creator cannot be removed");
        _etherealGuardians[guardian] = false;
        emit GuardianRemoved(guardian);
    }

    /// @notice Check if address is guardian
    /// @param guardian The address to check
    function isGuardian(address guardian) external view returns (bool) {
        return _etherealGuardians[guardian];
    }
}

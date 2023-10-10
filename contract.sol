// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract Ledger {
    struct Entry {
        address sender;
        string description;
        uint256 amount;
    }

    Entry[] public entries;

    event EntryAdded(address indexed sender, string description, uint256 amount);

    function addEntry(string memory description, uint256 amount) public {
        Entry memory newEntry = Entry(msg.sender, description, amount);
        entries.push(newEntry);
        emit EntryAdded(msg.sender, description, amount);
    }

    function getEntryCount() public view returns (uint256) {
        return entries.length;
    }

    function getEntry(uint256 index) public view returns (address, string memory, uint256) {
        require(index < entries.length, "Entry does not exist");
        Entry memory entry = entries[index];
        return (entry.sender, entry.description, entry.amount);
    }
}

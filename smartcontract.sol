pragma solidity ^0.8.0;

contract MyToken {
    mapping(address => uint256) public balances;

    function transfer(address recipient, uint256 amount) public {
        balances[msg.sender] -= amount;
        balances[recipient] += amount;
    }
}

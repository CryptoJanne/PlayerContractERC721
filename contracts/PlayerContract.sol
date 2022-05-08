pragma solidity ^0.8.4;

import "@openzeppelin/contracts/token/ERC721/ERC721.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/Counters.sol";
import "@openzeppelin/contracts/token/ERC721/extensions/ERC721Enumerable.sol";

contract Player is ERC721, Ownable, ERC721Enumerable {
using Counters for Counters.Counter;

Counters.Counter private _tokenIdCounter;

constructor() ERC721("Player", "plr") 
{

}
// uint = unsigned integer, from 0 to 2^256 - 1
// int = signed integer, half value before 0 and half after. maximum positive = 2^256 / 2 - 1 maximum negative = negative 2^256 / 2 - 1
struct Player
{
    string name; // Name of the Player
    uint level; // Player Level
    uint8 race;  // 1 = normal, 2 = rare, 3 = epic, 4 = legendary
    uint id;
}

mapping(uint => Player) players; // First Player has Index 0

function createPlayer(string memory _name, address _to, uint level, uint8 race) public
{
    uint num = _tokenIdCounter.current();
    players[num].name = _name;
    players[num].level = level;
    players[num].race = race;
    players[num].id = num;
    _safeMint(_to, num);
    _tokenIdCounter.increment();
}


function getPlayer(uint player) public view returns(string memory _name, uint level, uint8 race, uint id)
{
    uint level = players[player].level;
    uint8 race = players[player].race;
    uint id = players[player].id;
    string memory _name = players[player].name;
    return(_name, level, race, id);
}

function _beforeTokenTransfer(address from, address to, uint256 tokenId) internal override(ERC721, ERC721Enumerable)
{
    super._beforeTokenTransfer(from, to, tokenId);
}

function supportsInterface(bytes4 interfaceId) public view override(ERC721, ERC721Enumerable) returns (bool)
{
    return super.supportsInterface(interfaceId);
}
}
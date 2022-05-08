import time
from turtle import back
from brownie import Player, accounts, network, config
from scripts.helpers import get_account, get_account2
## when using ganache use:
# ganache-cli --chain.hardfork istanbul
def main():
    account = get_account()
    account2 = get_account2()
    bajs = Player.deploy({"from": account})
    #string memory _name, address _to, uint level, uint rarityLevel,uint id
    bajs.createPlayer("bajs", account2, 10, 5, {"from": account})
    bajs.createPlayer("korv", account2, 2, 1, {"from": account})
    #function getItem(uint item)
    print(bajs.getPlayer(0))
    print(bajs.getPlayer(1))
    print(bajs.balanceOf(account2))
    print(bajs.balanceOf(account))
    #bajs.transferShit(account2, account, {"from": account})
    bajs.safeTransferFrom(account2, account, 1, {"from": account2})
    print(bajs.balanceOf(account))
    print(bajs.balanceOf(account2))
    print(bajs.getPlayer(0))
    print(bajs.getPlayer(1))
    #tokenOfOwnerByIndex(address owner, uint256 index)
    kuk = bajs.tokenOfOwnerByIndex(account, 0)
    print(kuk)
    print(bajs.getPlayer(kuk))
    merkuk = bajs.tokenOfOwnerByIndex(account2, 0)
    print(bajs.getPlayer(merkuk))
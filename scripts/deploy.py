import time
from brownie import Item, accounts, network, config
from scripts.helpers import get_account, get_account2
## when using ganache use:
# ganache-cli --chain.hardfork istanbul
def main():
    account = get_account()
    account2 = get_account2()
    bajs = Item.deploy({"from": account})
    #bajs.safeMint(account, {"from": account})
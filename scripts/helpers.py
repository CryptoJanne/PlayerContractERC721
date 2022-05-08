from brownie import network, config, accounts

def get_account():
    if(network.show_active() == "development"):
        return accounts[0]
    else:
        return accounts.add(config["wallets"]["from_key"])

def get_account2():
    if(network.show_active() == "development"):
        return accounts[1]
    else:
        return accounts.add(config["wallets"]["from_key2"])
from brownie import accounts, config, SimpleStorage, network
import os


def deploy_simple_storage():
    # account = accounts[0]
    # account = accounts.load("my-account")
    # account = accounts.add(os.getenv("PRIVATE_KEY_ETH"))
    # account = accounts.add(config['wallets']['from_key'])
    account = get_account()
    simple_storage = SimpleStorage.deploy({"from": account})
    stored_value = simple_storage.retrieve()
    print(stored_value)
    tx = simple_storage.store(15, {"from": account})
    tx.wait(1)
    updated_value = simple_storage.retrieve()
    print(updated_value)


def get_account():
    if network.show_active() == "development":
        return accounts[0]
    return accounts.load("my-account")


def main():
    deploy_simple_storage()

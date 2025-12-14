import boa
from boa.network import NetworkEnv, EthereumRPC
from dotenv import load_dotenv
import os
from eth_account import Account

MY_CONTRACT_ADDRESS = "0xCf7Ed3AccA5a467e9e704C703E8D87F634fB0Fc9"

load_dotenv()

def main():
    print("Interact with the deployed favorites contract.")

    rpc_url = os.getenv("RPC_URL", "http://127.0.0.1:8545")
    env = NetworkEnv(EthereumRPC(rpc_url))
    boa.set_env(env)

    my_account = Account.from_key(os.getenv("ANVIL_PRIVATE_KEY"))
    boa.env.add_account(my_account, force_eoa=True)   

    favorite_deployer = boa.load_partial("favorites.vy")
    favorites_contract = favorite_deployer.at(MY_CONTRACT_ADDRESS)

    current_favorite_number = favorites_contract.retrieve()
    print(f"Current favorite number is: {current_favorite_number}")
    # tx = favorites_contract.store(7, sender=my_account.address)
    # updated_favorite_number = favorites_contract.retrieve()
    # print(f"Updated favorite number is: {updated_favorite_number}")


if __name__ == "__main__":
    main()
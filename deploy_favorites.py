import boa
from boa.network import NetworkEnv, EthereumRPC
from dotenv import load_dotenv
import os
from eth_account import Account

load_dotenv()

def main():
    print("Read the vyper code and deploy the contract using anvil.")

    rpc_url = os.getenv("RPC_URL", "http://127.0.0.1:8545")

    env = NetworkEnv(EthereumRPC(rpc_url))

    boa.set_env(env)

    my_account = Account.from_key(os.getenv("ANVIL_PRIVATE_KEY"))

    boa.env.add_account(my_account, force_eoa=True)   

    favorites_contract = boa.load("favorites.vy")

    starting_favorite_number = favorites_contract.retrieve()
    print(f"Starting favorite number is: {starting_favorite_number}")

    tx = favorites_contract.store(42, sender=my_account.address)

    updated_favorite_number = favorites_contract.retrieve()
    print(f"Updated favorite number is: {updated_favorite_number}")
    
    
    print("Deployment complete.")


if __name__ == "__main__":
    main()# deploy_favorites.py
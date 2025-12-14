import boa
from boa.network import NetworkEnv, EthereumRPC
from dotenv import load_dotenv
import os

load_dotenv()

def main():
    rpc_url = os.getenv("RPC_URL")
    print("Read the vyper code and deploy the contract using anvil.")
    favorites_contract = boa.load("favorites.vy")

    starting_favorite_number = favorites_contract.retrieve()
    print(f"Starting favorite number is: {starting_favorite_number}")
    
    # print("Deployment complete.")


if __name__ == "__main__":
    main()# deploy_favorites.py
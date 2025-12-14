import boa

def main():
    print("Read the vyper code and deploy the contract using pyevm.")
    favorites_contract = boa.load("favorites.vy")

    starting_favorite_number = favorites_contract.retrieve()
    print(f"Starting favorite number is: {starting_favorite_number}")
    
    # print("Deployment complete.")


if __name__ == "__main__":
    main()# deploy_favorites_pyevm.py
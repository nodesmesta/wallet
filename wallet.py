import json

# File paths
input_file = 'wallets.json'
output_file = 'wallet.txt'

def format_wallets(input_path, output_path):
    try:
        # Read JSON file
        with open(input_path, 'r') as infile:
            data = json.load(infile)

        # Open output file for writing
        with open(output_path, 'w') as outfile:
            for wallet in data:
                address = wallet.get('address', 'N/A')
                private_key = wallet.get('private_key', 'N/A')
                outfile.write(f"{address} | {private_key}\n")

        print(f"Formatted wallets written to {output_path}")
    except FileNotFoundError:
        print(f"Error: The file {input_path} does not exist.")
    except json.JSONDecodeError:
        print("Error: Invalid JSON format in input file.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Execute the function
format_wallets(input_file, output_file)

from flask import Flask, render_template, request, redirect, url_for
from web3 import Web3
import json

app = Flask(__name__)

# Ethereum testnet configuration
infura_url = "https://goerli.infura.io/v3/INFURA_ID"
w3 = Web3(Web3.HTTPProvider(infura_url))

# Load the compiled Solidity contract ABI
contract_abi = [
	{
		"inputs": [
			{
				"internalType": "string",
				"name": "description",
				"type": "string"
			},
			{
				"internalType": "uint256",
				"name": "amount",
				"type": "uint256"
			}
		],
		"name": "addEntry",
		"outputs": [],
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"anonymous": False,
		"inputs": [
			{
				"indexed": True,
				"internalType": "address",
				"name": "sender",
				"type": "address"
			},
			{
				"indexed": False,
				"internalType": "string",
				"name": "description",
				"type": "string"
			},
			{
				"indexed": False,
				"internalType": "uint256",
				"name": "amount",
				"type": "uint256"
			}
		],
		"name": "EntryAdded",
		"type": "event"
	},
	{
		"inputs": [
			{
				"internalType": "uint256",
				"name": "",
				"type": "uint256"
			}
		],
		"name": "entries",
		"outputs": [
			{
				"internalType": "address",
				"name": "sender",
				"type": "address"
			},
			{
				"internalType": "string",
				"name": "description",
				"type": "string"
			},
			{
				"internalType": "uint256",
				"name": "amount",
				"type": "uint256"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "uint256",
				"name": "index",
				"type": "uint256"
			}
		],
		"name": "getEntry",
		"outputs": [
			{
				"internalType": "address",
				"name": "",
				"type": "address"
			},
			{
				"internalType": "string",
				"name": "",
				"type": "string"
			},
			{
				"internalType": "uint256",
				"name": "",
				"type": "uint256"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [],
		"name": "getEntryCount",
		"outputs": [
			{
				"internalType": "uint256",
				"name": "",
				"type": "uint256"
			}
		],
		"stateMutability": "view",
		"type": "function"
	}
]

# Replace this with your contract's address on the Goerli testnet
contract_address = "0x9F0E77B190b52AFe2413eFbe551e503DffD95f10"

# Ethereum account private key (replace with your private key)
private_key = "YOUR_PRIVATE_KEY"

# Connect to the Ethereum account
account = w3.eth.account.from_key(private_key)

# Create a contract instance
contract = w3.eth.contract(address=contract_address, abi=contract_abi)

@app.route("/")
def landing_page():
    entries = get_entries()
    return render_template("index.html", entries=entries)

@app.route("/add", methods=["POST"])
def add_entry():
    description = request.form["description"]
    amount = int(request.form["amount"])

    sender_account = w3.eth.account.from_key(private_key)
    nonce = w3.eth.get_transaction_count(sender_account.address)

    # Build the transaction
    transaction = contract.functions.addEntry(description, amount).buildTransaction({
        'chainId': 5,  # Goerli Testnet
        'gas': 2000000,  # Adjust gas limit as needed
        'gasPrice': w3.toWei('20', 'gwei'),  # Adjust gas price as needed
        'nonce': nonce,
    })

    # Sign the transaction
    signed_transaction = w3.eth.account.signTransaction(transaction, private_key)

    # Send the transaction
    transaction_hash = w3.eth.sendRawTransaction(signed_transaction.rawTransaction)

    # Wait for the transaction to be mined
    w3.eth.waitForTransactionReceipt(transaction_hash)

    return redirect(url_for("landing_page"))

def get_entries():
    entry_count = contract.functions.getEntryCount().call()
    entries = []
    for i in range(entry_count):
        entry = contract.functions.getEntry(i).call()
        entries.append(entry)
    return entries

if __name__ == "__main__":
    app.run(debug=True)

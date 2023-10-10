# Ledger Web Application

![Screenshot (46)](https://github.com/ayushete02/Tegro/assets/75811912/61c89e5d-dfa3-470f-96de-121419420408)

This is a simple web application for recording ledger entries on the Ethereum Goerli testnet.

## Table of Contents

- [Prerequisites](#prerequisites)
- [Setup](#setup)
- [Running the Application](#running-the-application)
- [Usage](#usage)
- [Deployment](#deployment)
- [Transaction History](#transaction-history)
- [Snapshots](#snapshots)

## Prerequisites

Before running the application, make sure you have the following installed:

- Python (version 3.6 or higher)
- Flask (a Python web framework)
- web3.py (for interacting with Ethereum)
- An Ethereum account private key
- Infura API key (for Ethereum connectivity)

## Setup

1. **Clone this repository** to your local machine:

   ```bash
   git clone https://github.com/your-username/ledger-web-app.git
   cd ledger-web-app 
   ```

2. **Install the required Python packages** using pip:

   ```bash 
   pip install -r requirements.txt
   ```

3. Set up your **Ethereum private key** and **Infura API key**:

- Replace "YOUR_PRIVATE_KEY" with your Ethereum account's private key in app.py.
- Replace "https://goerli.infura.io/v3/INFURA_ID" with your Infura API key in app.py.

## Running the Application

To start the web application, run the following command:

  ```bash
   python app.py
   ```
The application will be accessible at http://127.0.0.1:5000 in your web browser.


## Usage
- **Visit** http://127.0.0.1:5000 in your web browser.

- Add Ledger Entries:
- - Provide a description and amount.
- - Click the "Add Entry" button.

- View Ledger Entries:

- - The ledger entries will be displayed on the page.

- Transaction Feedback:
- - Transaction feedback messages will appear at the bottom of the page.

## Deployment
To deploy this application to a production server, consider the following:

- Securely store your private key and sensitive information.
- Use a production-ready WSGI server (e.g., Gunicorn) instead of Flask's built-in server.

## Transaction History
You can view the transaction history for the smart contract on the Goerli testnet on Etherscan.

URL: https://goerli.etherscan.io/address/0x9f0e77b190b52afe2413efbe551e503dffd95f10

## Snapshots
![Screenshot (46)](https://github.com/ayushete02/Tegro/assets/75811912/23455b7c-36e3-44b4-8168-cdc9ff61d45e)
![Screenshot (45)](https://github.com/ayushete02/Tegro/assets/75811912/b7e29dbe-65ea-494d-8c53-057fdb255342)

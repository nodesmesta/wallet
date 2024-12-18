# Wallet Application

This repository contains a Python application for processing wallet JSON files and formatting them into a readable text format.

## Features
- Reads a JSON file containing wallet information.
- Formats the output into a `wallet.txt` file with a `pubkey | private key` structure.

## Installation and Usage

Follow these steps to install and use the application on Ubuntu 22.04:

### 1. Prerequisites
Ensure that Python 3.x and Git are installed on your system. You can install them using the following commands:

```bash
sudo apt update
sudo apt install python3 python3-pip git -y
```

### 2. Clone the Repository

Clone this repository into your desired directory:

```bash
git clone https://github.com/nodesmesta/wallet.git
cd wallet
```

### 3. Install Dependencies

If the repository has a `requirements.txt` file, install the necessary dependencies:

```bash
pip3 install -r requirements.txt
```


### 4. Run the Application

Run the script to process the JSON file and generate the `wallet.txt` output:

```bash
python3 wallet.py
```

The file will display the wallet addresses and private keys in the format:

```
pubkey | privatekey
```

## License

Copyright © Nodesemesta. All rights reserved.

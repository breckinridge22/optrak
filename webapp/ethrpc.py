import json
import web3

from web3 import Web3, HTTPProvider, TestRPCProvider
from solc import compile_source
from web3.contract import ConciseContract
from django.conf import settings

settings.configure(DEBUG=True)
# TODO: Refactor all the string constants to ENV settings variables

# Solidity source code
contract_source_code = open('./contracts/Optrak.sol', 'r').read()

compiled_sol = compile_source(contract_source_code) # Compiled source code
contract_interface = compiled_sol['<stdin>:Optrak']

# web3.py instance
w3 = Web3(HTTPProvider('http://testrpc:8545')) # TODO: configure settings and change this to settings.TESTRPC_URL

# Instantiate and deploy contract
contract = w3.eth.contract(contract_interface['abi'], bytecode=contract_interface['bin'])

# Get transaction hash from deployed contract
tx_hash = contract.deploy(transaction={'from': w3.eth.accounts[0], 'gas': 3000000})

# Get tx receipt to get contract address
tx_receipt = w3.eth.getTransactionReceipt(tx_hash)
contract_address = tx_receipt['contractAddress']

# Contract instance in concise mode
contract_instance = w3.eth.contract(contract_interface['abi'], contract_address, ContractFactoryClass=ConciseContract)

# Getters + Setters for web3.eth.contract object
contract_instance.addProvider('dr who', 'pubkey', transact={'from': w3.eth.accounts[0]})
print('Setting provider to: dr who')
print('Contract value: {}'.format(contract_instance.getProviderPubkey('dr who')))
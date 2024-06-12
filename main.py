from web3 import Web3

one = Web3.to_wei(1, 'ether')
two = Web3.from_wei(500000000, 'gwei')

print(f'one: {one} \ntwo: {two}')

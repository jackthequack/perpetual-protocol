from brownie import accounts, ZERO_ADDRESS
from brownie.network.gas.strategies import GasNowScalingStrategy

def main():

	deployer = accounts[10]
	balance = deployer.balance()
	gas_strategy = GasNowScalingStrategy()

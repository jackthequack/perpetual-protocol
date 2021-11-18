
import brownie

from brownie import (
    accounts,
    Contract,
    project,
    network,
    Amm,
    ClearingHouse,
    ChainlinkPriceFeed,
    InsuranceFund,
    MetaTxGateway


)

from brownie.network.gas.strategies import GasNowScalingStrategy
from math import floor, sqrt
import time

PriceFeedAggregator = "0x5f4ec3df9cbd43714fe2740f5e3616155c5b8419" #Chainlink ETH price feed aggregator.
PriceFeedKeyinHex = 0x455448

def main():

    deployer = accounts[10]

    gas_strategy = GasNowScalingStrategy()
    network.gas_limit(6700000)

    AMM = deployer.deploy(Amm)
    CH = deployer.deploy(ClearingHouse)
    PriceFeed = deployer.deploy(ChainlinkPriceFeed)
    InsFund = deployer.deploy(InsuranceFund)
    MetaTx = deployer.deploy(MetaTxGateway)

    Agg = Contract.from_explorer(PriceFeedAggregator, owner=deployer)

    PriceFeed.initialize({'from': deployer})
    PriceFeed.addAggregator(PriceFeedKeyinHex, Agg.address, {'from': deployer})

    AMM.initialize(1000, 100, 1, 86400, PriceFeed.address, 0x455448, "0xa0b86991c6218b36c1d19d4a2e9eb0ce3606eb48", 0, 0, 0, {'from': deployer})

    InsFund.initialize({'from': deployer})

    MetaTx.initialize("Perp", "1", 1, {'from': deployer})

    CH.initialize(.05, .05, .05, InsFund.address, MetaTx.address, {'from': deployer})


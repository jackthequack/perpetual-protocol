import brownie
from brownie import (
    accounts,
    project,
    Amm,
    ClearingHouse
)

from brownie.network.gas.strategies import GasNowScalingStrategy
from math import floor, sqrt
import time


def main():
    deployer = accounts[10]

    gas_strategy = GasNowScalingStrategy()
    AMM = deployer.deploy(Amm)
    AMM.initialize(1, 1, 1, 1, "0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2", 1, 1, 1)
    CH = deployer.deploy(ClearingHouse)
    CH.initialize(100000000000000000, 62500000000000000, 12500000000000000)
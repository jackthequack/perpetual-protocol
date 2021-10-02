# Perpetual Protocol

## Bronwie Framework

## Installing

- [Install Brownie](https://eth-brownie.readthedocs.io/en/stable/install.html)

```
# install and activate the virtual environment
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

```
# brownie clone peripheries
brownie pm clone OpenZeppelin/openzeppelin-contracts@3.4.0
brownie pm install smartcontractkit/chainlink-brownie-contracts@0.2.2
```

## Getting Started

```
brownie compile
brownie test
```

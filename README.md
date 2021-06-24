# Obelisk

A proof of concept command line ethereum wallet written in python.

## Description

As my interest in crypto-currencies has grown I wanted to dip my toe into what 
I could develop given some basic libraries and my knowledge of python. I thought
it best to start with a simple ethereum wallet which creates, migrates, and stores
encrypted wallets which can then send and receive payment. I do not recommend 
using this wallet as a daily driver, it currently lacks supports for ethereum
tokens, and the private key generation uses the standard random library. Although
this is fun to play around with, in the future I wish to create a wallet which
could be used as a main wallet using the code here as a good stepping stone. 

## Getting Started

### Dependencies

* Built using Python 3.8.5, should work on Python 3 and above
* Built on Linux, should also run on Windows and macOS

### Libraries/Modules

* requests 2.22.0
* bip_utils 1.6.0
* web3 5.16.0
* qrcode 6.1
* beautifulsoup 4.9.3
* Pillow 8.1.0
* pycryptodome 3.10.1

### Installing

* Download the repository 
* Unzip the repository into the desired location

### Executing Program

* cd into the folders location
* cd into Obelisk-Python-Wallet
* Run the Command:
```
python obelisk.py
```

## Authors

Jack Sanderson
[@JackASanderson](https://twitter.com/JackASanderson)

## Acknowledgments

Inspiration, code snippets, etc.
* [ethereum.org](https://ethereum.org/en/)
* [web3 Python Library](https://web3py.readthedocs.io/en/stable/)
* [Public Key Generation Method](https://www.youtube.com/watch?v=iB3HcPgm_FI)
* [BIP Utility Library](https://pypi.org/project/bip-utils/)

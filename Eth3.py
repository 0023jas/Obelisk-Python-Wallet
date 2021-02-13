from web3 import Web3
from pubKeyGen import EccMultiply, GPoint
from privKeyGen import genPrivKey
from walletDecryption import walletDecryption
import os
import time
import glob

#Used to store and encrypt wallet
from Crypto.Cipher import AES
from Crypto.Protocol.KDF import scrypt
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes
import json

#Individual Transaction/Personal Information
def createWallet():
  os.system('cls')
  print("╔═╗┌─┐┌┐┌┌─┐┬─┐┌─┐┌┬┐┌─┐  ╦ ╦┌─┐┬  ┬  ┌─┐┌┬┐")
  print("║ ╦├┤ │││├┤ ├┬┘├─┤ │ ├┤   ║║║├─┤│  │  ├┤  │ ")
  print("╚═╝└─┘┘└┘└─┘┴└─┴ ┴ ┴ └─┘  ╚╩╝┴ ┴┴─┘┴─┘└─┘ ┴ ")
  print("")
  print("############################################")
  print("")
  print("> Please Input a Secure Password")
  print("")
  password = input("> ")
  time.sleep(2)

  print("")
  print("> Generating Wallet")
  privKey = genPrivKey() 

  PublicKey = EccMultiply(GPoint,privKey)
  PublicKey = hex(PublicKey[0])[2:] + hex(PublicKey[1])[2:]

  address = Web3.keccak(hexstr = PublicKey).hex()
  address = "0x" + address[-40:]
  address = Web3.toChecksumAddress(address)
  time.sleep(2)

  print("")
  print("> Encrypting Wallet")
  salt = get_random_bytes(16)
  key = scrypt(password, salt, 32, N=2**20, r = 8, p = 1)
  privKey = hex(privKey)[2:]
  data = str(privKey).encode('utf-8')

  cipher = AES.new(key, AES.MODE_CBC)
  ct_bytes = cipher.encrypt(pad(data, AES.block_size))

  salt = salt.hex()
  iv = cipher.iv.hex()
  ct = ct_bytes.hex()

  output = {"salt" : salt, "initialization vector" : iv, "encrypted private key" : ct}

  with open("wallets/" + address + '.txt', 'w') as json_file:
    json.dump(output, json_file) 
  
  print("")
  print("> Wallet Created")
  time.sleep(2)


def decodeWallet():
  walletSelect = False
  while walletSelect == False:
    os.system('cls')
    print(" ╔═╗┌─┐┬  ┌─┐┌─┐┌┬┐  ╦ ╦┌─┐┬  ┬  ┌─┐┌┬┐")
    print(" ╚═╗├┤ │  ├┤ │   │   ║║║├─┤│  │  ├┤  │")
    print(" ╚═╝└─┘┴─┘└─┘└─┘ ┴   ╚╩╝┴ ┴┴─┘┴─┘└─┘ ┴")
    print("")
    print(" ############################################")
    print("")

    availableWallets = os.listdir("wallets")
    for wallet in range(len(availableWallets)):
      print(" " + str(wallet+1) + ": " + availableWallets[wallet][:-4])
      print("")

    walletSelector = input(" > ")

    if 0 < int(walletSelector) <= len(availableWallets):
      
      walletName = availableWallets[int(walletSelector)-1]
      with open("wallets/" + walletName) as f:
        data = json.load(f)

      print("Enter Password:")
      password = input(" > ")
      address = walletName[:-4]
      walletSelect = True
      walletDecryption(password, data, address)


def startWallet():
  userOption = False
  while(userOption == False):
    os.system('cls')
    print("")
    print("  ██████╗ ██████╗ ███████╗██╗     ██╗███████╗██╗  ██╗")
    print(" ██╔═══██╗██╔══██╗██╔════╝██║     ██║██╔════╝██║ ██╔╝")
    print(" ██║   ██║██████╔╝█████╗  ██║     ██║███████╗█████╔╝ ")
    print(" ██║   ██║██╔══██╗██╔══╝  ██║     ██║╚════██║██╔═██╗ ")
    print(" ╚██████╔╝██████╔╝███████╗███████╗██║███████║██║  ██╗")
    print("  ╚═════╝ ╚═════╝ ╚══════╝╚══════╝╚═╝╚══════╝╚═╝  ╚═╝")
    print("")
    print(" ####################################################")
    print("")
    print(" 1: Generate New Wallet")
    print("")
    print(" 2: Access Saved Wallet")
    print("")
    userInput = input(" > ")
    if userInput != "1" and userInput != "2":
      os.system('cls')
      print("> Oops, wrong input!")
      print("")
      print("> 1 or 2 is the only acceptable input")
      time.sleep(5)
    else:
      userOption = True
  
  if userInput == "1":
    createWallet()
  elif userInput == "2":
    decodeWallet()
  
startWallet()


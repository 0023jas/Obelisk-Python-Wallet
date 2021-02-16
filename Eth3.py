from web3 import Web3
from pubKeyGen import EccMultiply, GPoint
from privKeyGen import genPrivKey
from walletDecryption import walletDecryption
from walletInteractions import getEth
import os
import time
import glob

#Used to store and encrypt wallet
from Crypto.Cipher import AES
from Crypto.Protocol.KDF import scrypt
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes
import json

#Used for Bip39Mnemonic
from bip_utils import Bip39MnemonicGenerator, Bip39SeedGenerator, Bip44, Bip44Coins, Bip44Changes


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
    print(" ######################################")
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
      print(data)

      print("Enter Password:")
      password = input(" > ")
      address = walletName[:-4]
      walletSelect = True
      walletDecryption(password, data, address)


def migrateWallet():
  os.system('cls')
  print(" ╔╦╗┬┌─┐┬─┐┌─┐┌┬┐┌─┐  ╦ ╦┌─┐┬  ┬  ┌─┐┌┬┐")
  print(" ║║║││ ┬├┬┘├─┤ │ ├┤   ║║║├─┤│  │  ├┤  │ ")
  print(" ╩ ╩┴└─┘┴└─┴ ┴ ┴ └─┘  ╚╩╝┴ ┴┴─┘┴─┘└─┘ ┴ ")
  print("")
  print(" #######################################")
  print("")
  print(" 1: Migrate Through Private Key")
  print("")
  print(" 2: Migrate Through 12 Word Phrase")
  print("")
  userInput = input(" > ")
  print("")
  if userInput == "1":
    print(" Type Private Key:")
    print("")
    privKey = input(" > ")
    privKey = int(privKey, 16)
    print("")
    print(" Type Strong Password:")
    print("")
    password = input(" > ")
  
    PublicKey = EccMultiply(GPoint, privKey)
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
    startWallet()

  elif userInput == "2":
    print(" Type 12 Words:")
    mnemonic = input(" > ")
    seed_bytes = Bip39SeedGenerator(mnemonic).Generate()
    bip_obj_mst = Bip44.FromSeed(seed_bytes, Bip44Coins.ETHEREUM)
    bip_obj_acc = bip_obj_mst.Purpose().Coin().Account(0)
    bip_obj_chain = bip_obj_acc.Change(Bip44Changes.CHAIN_EXT)
    accountFound = False
    accountNumber = 0
    while accountFound == False:
      bip_obj_addr = bip_obj_chain.AddressIndex(accountNumber)
      checkAddress = getEth(bip_obj_addr.PublicKey().ToAddress())
      if checkAddress > 0:
        accountFound = True
        privKey = bip_obj_addr.PrivateKey().Raw().ToHex()
        privKey = int(privKey, 16)
        print("")
        print(" > Found Wallet!")
        time.sleep(2)
    
    print("")
    print(" Type Strong Password:")
    print("")
    password = input(" > ")

    PublicKey = EccMultiply(GPoint, privKey)
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
    startWallet()


    

    


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
    print(" 1: Access Saved Wallet")
    print("")
    print(" 2: Generate New Wallet")
    print("")
    print(" 3: Migrate Wallet")
    print("")
    userInput = input(" > ")
    if userInput != "1" and userInput != "2" and userInput != "3":
      os.system('cls')
      print("")
      print(" > Oops, wrong input!")
      print("")
      print(" > 1 or 2 is the only acceptable input")
      print("")
      print(" > Hit enter to continue")
      print("")
      errorInput = input(" > ")
    else:
      userOption = True
  
  if userInput == "1":
    decodeWallet()
  elif userInput == "2":
    createWallet()
  elif userInput == "3":
    migrateWallet()
  
startWallet()


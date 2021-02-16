from Crypto.Cipher import AES
from Crypto.Protocol.KDF import scrypt
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes
import json
import time
import os

from walletInteractions import sendEth, getEth, receiveEth
from currencyConvert import weiToEth


def runWallet(privateKey, address):
  os.system('cls')
  print("")
  print(" ╔═╗┌┐ ┌─┐┬  ┬┌─┐┬┌─  ╦ ╦┌─┐┬  ┬  ┌─┐┌┬┐")
  print(" ║ ║├┴┐├┤ │  │└─┐├┴┐  ║║║├─┤│  │  ├┤  │ ")
  print(" ╚═╝└─┘└─┘┴─┘┴└─┘┴ ┴  ╚╩╝┴ ┴┴─┘┴─┘└─┘ ┴ ")
  print("")
  print(" #######################################")
  print("")
  print(" Address: " + address)
  print(" Wallet Value: " + str(weiToEth(getEth(address))))
  print("")
  print(" Actions: ")
  print(" 1: Send")
  print(" 2: Receive")
  print(" 3: Exit")
  print("")
  userQuit = False
  while userQuit == False:
    userInput = input(" > ")
    if userInput == "1":
      sendEth(privateKey, address)
    elif userInput == "2":
      receiveEth(address)
    elif userInput == "3":
      os.system('cls')
      userQuit = True


def walletDecryption(password, data, address):
  salt = data['salt']
  iv = data['initialization vector'] 
  ct = data['encrypted private key']

  salt = bytes.fromhex(salt)
  iv = bytes.fromhex(iv)
  ct = bytes.fromhex(ct)

  key = scrypt(password, salt, 32, N = 2**20, r = 8, p = 1)
  cipher = AES.new(key, AES.MODE_CBC, iv)

  #try:
  pt = unpad(cipher.decrypt(ct), AES.block_size)
  privateKey = pt.decode('utf-8')
  print(privateKey)
  time.sleep(5)
  runWallet(privateKey, address)
  """
  except:
    print("wrong password entered")
    time.sleep(5)
  """
from Crypto.Cipher import AES
from Crypto.Protocol.KDF import scrypt
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes
import json
import time
import os

from walletInteractions import sendEth, getEth, receiveEth
from currencyConvert import weiToEth

#Used to run getWalletStats
import requests
from bs4 import BeautifulSoup
import re
import requests

def getWalletStats():
  statsList = []

  #Get Ethereum Value
  ethLink = requests.get('https://coinmarketcap.com/currencies/ethereum/')
  ethSoup = BeautifulSoup(ethLink.content, 'html.parser')
  ethPrice = ethSoup.findAll('td')
  ethPrice = ethPrice[0].contents
  ethPrice = re.sub('\ USD$', '', ethPrice[0])
  ethPrice = ethPrice[1:]
  ethPrice = float(ethPrice.replace(',',''))
  statsList.append(ethPrice)
  
  #Get Low, Medium, and High Gas Fees
  gasLink = requests.get('https://ethgasstation.info/')
  gasSoup = BeautifulSoup(gasLink.content, 'html.parser')
  lowFee = gasSoup.find('div', {'class':'safe_low'})
  avgFee = gasSoup.find('div', {'class':'standard'})
  highFee = gasSoup.find('div', {'class':'fast'})

  statsList.append(int(lowFee.contents[0]))
  statsList.append(int(avgFee.contents[0]))
  statsList.append(int(highFee.contents[0]))

  return statsList



def runWallet(privateKey, address):
  userQuit = False
  while userQuit == False:
    os.system('cls' if os.name == 'nt' else 'clear')

    ethStats = getWalletStats()

    walletEthereumValue = round(weiToEth(getEth(address)), 6)
    walletDollarValue = round(walletEthereumValue * ethStats[0], 2)

    lowGas = ethStats[1]
    avgGas = ethStats[2]
    highGas = ethStats[3]

    print("")
    print(" ╔═╗┌┐ ┌─┐┬  ┬┌─┐┬┌─  ╦ ╦┌─┐┬  ┬  ┌─┐┌┬┐")
    print(" ║ ║├┴┐├┤ │  │└─┐├┴┐  ║║║├─┤│  │  ├┤  │ ")
    print(" ╚═╝└─┘└─┘┴─┘┴└─┘┴ ┴  ╚╩╝┴ ┴┴─┘┴─┘└─┘ ┴ ")
    print("")
    print(" #######################################")
    print("")
    print(" Address: " + address)
    print(" Ethereum Value: Ξ" + str(walletEthereumValue))
    print(" Dollar Value: $" + str(walletDollarValue))
    print("")
    print(" Current Gas Prices in Gwei:")
    print(" Low: " + str(lowGas) + ", Average: " + str(avgGas) + ", High: " + str(highGas))
    print("")
    print(" Actions: ")
    print(" 1: Send")
    print(" 2: Receive")
    print(" 3: Exit")
    print("")
  
    userInput = input(" > ")
    if userInput == "1":
      sendEth(privateKey, address)
    elif userInput == "2":
      receiveEth(address)
    elif userInput == "3":
      os.system('cls' if os.name == 'nt' else 'clear')
      userQuit = True


def walletDecryption(data, address):
  correctPassword = False
  while correctPassword == False:
    print("")
    print(" Enter Password or type n to return:")
    print("")
    password = input(" > ")

    salt = data['salt']
    iv = data['initialization vector'] 
    ct = data['encrypted private key']

    salt = bytes.fromhex(salt)
    iv = bytes.fromhex(iv)
    ct = bytes.fromhex(ct)

    key = scrypt(password, salt, 32, N = 2**20, r = 8, p = 1)
    cipher = AES.new(key, AES.MODE_CBC, iv)

    try:
      pt = unpad(cipher.decrypt(ct), AES.block_size)
      privateKey = pt.decode('utf-8')
      #print(privateKey)
      #time.sleep(5)
      correctPassword = True
      runWallet(privateKey, address)

    except:
      if password == 'n':
        correctPassword = True
        print("")
        print(" > Returning to home")
        time.sleep(2)

      else:
        print("")
        print(" > wrong password entered")
        time.sleep(2)

  
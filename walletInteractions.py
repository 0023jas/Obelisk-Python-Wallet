from web3 import Web3
from PIL import Image
from currencyConvert import ethToWei, gweiToWei
import time

w3 = Web3(Web3.HTTPProvider('https://mainnet.infura.io/v3/5d6be6c002c744358836ac43f459d453'))

def getEth(address):
  return w3.eth.get_balance(address)

def sendEth(privateKey, address):

  #Typed as String must Remain String
  print("")
  print(" Enter the Receiver Address:")
  receiveAddress = input(" > ")

  #Typed in Eth needs to be Wei
  print("")
  print(" Enter the Amount you Want to Send in Eth:")
  sendAmount = int(ethToWei(float(input(" > "))))
  #print(sendAmount)

  #Typed in Gwei needs to be wei
  print("")
  print(" Type Gas Fee in Gwei:")
  gasFee = gweiToWei(int(input(" > ")))

  signed_txn = w3.eth.account.signTransaction(dict(
      nonce=w3.eth.getTransactionCount(address),
      gasPrice=gasFee,
      gas=21000,
      to=receiveAddress,
      value=sendAmount,
      data=b'',
    ),
    privateKey,
  )
  w3.eth.sendRawTransaction(signed_txn.rawTransaction)
  print("")
  print("Your transaction is sent! check it out here: etherscan.io/address/"+address)
  time.sleep(10)


def receiveEth(address):
  print("")
  print(" Wallet Address: " + address)
  print("")
  image = Image.open('qr/' + address + ".png")
  image.show()
  time.sleep(5)

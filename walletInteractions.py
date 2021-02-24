from web3 import Web3
from PIL import Image

w3 = Web3(Web3.HTTPProvider('https://mainnet.infura.io/v3/5d6be6c002c744358836ac43f459d453'))

def getEth(address):
  return w3.eth.get_balance(address)

def sendEth(privateKey, address):

  #Typed as String must Remain String
  print(" Enter the Receiver Address")
  receiveAddress = input(" > ")

  #Typed in Eth needs to be Wei
  print(" Enter the amount you want to send in Eth:")
  sendAmount = int(input(" > "))

  #Typed in Wei needs to be Gwei
  print(" Type Gas Fee:")
  gasFee = int(input(" > "))

  signed_txn = w3.eth.account.signTransaction(dict(
      nonce=w3.eth.getTransactionCount(address),
      gasPrice=gasFee,
      gas=100000,
      to=receiveAddress,
      value=sendAmount,
      data=b'',
    ),
    privateKey,
  )
  print(w3.eth.sendRawTransaction(signed_txn.rawTransaction))


def receiveEth(address):
  print("")
  print(" Wallet Address: " + address)
  print("")
  image = Image.open('qr/' + address + ".png")
  image.show()

import tweepy
import requests
from bs4 import BeautifulSoup
import re
import time

consumer_key = "9xjbdDvTmiOJSUdEN5R2YhSIU"
consumer_secret = "CojJvTd03ZmEUPPTvLEr2Z1lCXVW4eMnnT9llb67h6WsFFvQQ1"
access_token = "1121813086611169280-JYkliSbu2r2OJNUE9LoQlSWUTclunr"
access_token_secret = "LxPzPtCmRLB0ghhvD9EWinRwsTAfwxFjnPaLpABb8Pdft"

# authorization of consumer key and consumer secret 
auth = tweepy.OAuthHandler(consumer_key, consumer_secret) 
  
# set access to user's access key and access secret  
auth.set_access_token(access_token, access_token_secret) 
  
# calling the api  
api = tweepy.API(auth) 

# get the price of btc
def getBtc():
  btcList = []

  #Getting Bitcoin Price 
  btcLink = requests.get('https://coinmarketcap.com/currencies/bitcoin/')
  btcSoup = BeautifulSoup(btcLink.content, 'html.parser')
  btcPrice = btcSoup.findAll('td')
  btcPrice = btcPrice[0].contents
  btcPrice = re.sub('\ USD$', '', btcPrice[0])
  btcPrice = btcPrice[1:]
  btcPrice = float(btcPrice.replace(',',''))
  btcList.append(btcPrice)

  #Getting Bitcoin Percent Change
  pcSoup = BeautifulSoup(btcLink.content, 'html.parser')
  btcChange = pcSoup.findAll('td')
  btcChange = btcChange[1].contents[1].contents[0].contents[1]
  btcChange = float(btcChange.replace('%', ''))

  #Checking if XRP is Negative
  pcSoup = BeautifulSoup(btcLink.content, 'html.parser')
  btcCheck = pcSoup.findAll('td')
  btcCheck = btcCheck[1].contents[0].contents[0][1]

  if btcCheck == "-":
    btcChange = btcChange * -1
    btcList.append(btcChange)
  else:
    btcList.append(btcChange)

  return btcList

#print(getBtc())

# get the price of ethereum
def getEth():
  ethList = []

  #Getting Ethereum Price
  ethLink = requests.get('https://coinmarketcap.com/currencies/ethereum/')
  ethSoup = BeautifulSoup(ethLink.content, 'html.parser')
  ethPrice = ethSoup.findAll('td')
  ethPrice = ethPrice[0].contents
  ethPrice = re.sub('\ USD$', '', ethPrice[0])
  ethPrice = ethPrice[1:]
  ethPrice = float(ethPrice.replace(',',''))
  ethList.append(ethPrice)

  #Getting Ethereum Percent Change
  pcSoup = BeautifulSoup(ethLink.content, 'html.parser')
  ethChange = pcSoup.findAll('td')
  ethChange = ethChange[1].contents[1].contents[0].contents[1]
  ethChange = float(ethChange.replace('%', ''))

  #Checking if XRP is Negative
  pcSoup = BeautifulSoup(ethLink.content, 'html.parser')
  ethCheck = pcSoup.findAll('td')
  ethCheck = ethCheck[1].contents[0].contents[0][1]

  if ethCheck == "-":
    ethChange = ethChange * -1
    ethList.append(ethChange)
  else:
    ethList.append(ethChange)

  return ethList

#print(getEth())

# get the price of ripple
def getXrp():
  xrpList = []

  #Getting XRP Price 
  xrpLink = requests.get('https://coinmarketcap.com/currencies/xrp/')
  xrpSoup = BeautifulSoup(xrpLink.content, 'html.parser')
  xrpPrice = xrpSoup.findAll('td')
  xrpPrice = xrpPrice[0].contents
  xrpPrice = re.sub('\ USD$', '', xrpPrice[0])
  xrpPrice = xrpPrice[1:]
  xrpPrice = float(xrpPrice.replace(',',''))
  xrpList.append(xrpPrice)

  #Getting XRP Percent Change
  pcSoup = BeautifulSoup(xrpLink.content, 'html.parser')
  xrpChange = pcSoup.findAll('td')
  xrpChange = xrpChange[1].contents[1].contents[0].contents[1]
  xrpChange = float(xrpChange.replace('%', ''))
  
  #Checking if XRP is Negative
  pcSoup = BeautifulSoup(xrpLink.content, 'html.parser')
  xrpCheck = pcSoup.findAll('td')
  xrpCheck = xrpCheck[1].contents[0].contents[0][1]

  if xrpCheck == "-":
    xrpChange = xrpChange * -1
    xrpList.append(xrpChange)
  else:
    xrpList.append(xrpChange)

  return xrpList

#print(getXrp())

# get the price of litecoin
def getLtc():
  ltcList = []

  #Getting LTC Price
  ltcLink = requests.get('https://coinmarketcap.com/currencies/litecoin/')
  ltcSoup = BeautifulSoup(ltcLink.content, 'html.parser')
  ltcPrice = ltcSoup.findAll('td')
  ltcPrice = ltcPrice[0].contents
  ltcPrice = re.sub('\ USD$', '', ltcPrice[0])
  ltcPrice = ltcPrice[1:]
  ltcPrice = float(ltcPrice.replace(',',''))
  ltcList.append(ltcPrice)

  #Getting LTC Percentage Change
  pcSoup = BeautifulSoup(ltcLink.content, 'html.parser')
  ltcChange = pcSoup.findAll('td')
  ltcChange = ltcChange[1].contents[1].contents[0].contents[1]
  ltcChange = float(ltcChange.replace('%', ''))

  #Checking if LTC is Negative
  pcSoup = BeautifulSoup(ltcLink.content, 'html.parser')
  ltcCheck = pcSoup.findAll('td')
  ltcCheck = ltcCheck[1].contents[0].contents[0][1] 

  if ltcCheck == "-":
    ltcChange = ltcChange * -1
    ltcList.append(ltcChange)
  else:
    ltcList.append(ltcChange)

  return ltcList

#print(getLtc())


# get the price of bitcoin cash
def getBch():
  bchList = []

  #Getting BCH Price
  bchLink = requests.get('https://coinmarketcap.com/currencies/bitcoin-cash/')
  bchSoup = BeautifulSoup(bchLink.content, 'html.parser')
  bchPrice = bchSoup.findAll('td')
  bchPrice = bchPrice[0].contents
  bchPrice = re.sub('\ USD$', '', bchPrice[0])
  bchPrice = bchPrice[1:]
  bchPrice = float(bchPrice.replace(',',''))
  bchList.append(bchPrice)

  #Getting BCH Percentage Change
  pcSoup = BeautifulSoup(bchLink.content, 'html.parser')
  bchChange = pcSoup.findAll('td')
  bchChange = bchChange[1].contents[1].contents[0].contents[1]
  bchChange = float(bchChange.replace('%', ''))

  #Checking if BCH is Negative
  pcSoup = BeautifulSoup(bchLink.content, 'html.parser')
  bchCheck = pcSoup.findAll('td')
  bchCheck = bchCheck[1].contents[0].contents[0][1] 

  if bchCheck == "-":
    bchChange = bchChange * -1
    bchList.append(bchChange)
  else:
    bchList.append(bchChange)

  return bchList

#print(getBch())


def formatUSD():
  formatList = []

  btcPrice = getBtc()[0]
  btcPrice = "{:,}".format(btcPrice)
  btcPrice = "#Bitcoin: " + "$" + btcPrice
  formatList.append(btcPrice)

  ethPrice = getEth()[0]
  ethPrice = "{:,}".format(ethPrice)
  ethPrice = "#Ethereum: " + "$" + ethPrice
  formatList.append(ethPrice)

  xrpPrice = getXrp()[0]
  xrpPrice = "{:,}".format(xrpPrice)
  xrpPrice = "#Ripple: " + "$" + xrpPrice
  formatList.append(xrpPrice)

  ltcPrice = getLtc()[0]
  ltcPrice = "{:,}".format(ltcPrice)
  ltcPrice = "#Litecoin: " + "$" + ltcPrice
  formatList.append(ltcPrice)

  bchPrice = getBch()[0]
  bchPrice = "{:,}".format(bchPrice)
  bchPrice = "#BitcoinCash: " + "$" + bchPrice
  formatList.append(bchPrice)

  return formatList

#print(formatUSD())

def formatRelative():
  relativeList = []

  #Get Ethereum
  EthBtc = round(getEth()[0]/getBtc()[0], 4)
  EthBtc = "#Ethereum: " + "₿" + str(EthBtc) 
  relativeList.append(EthBtc)
  EthBtcPc = round(getEth()[1]-(getBtc()[1]), 2)
  relativeList.append(EthBtcPc)

  #Get Litecoin
  LtcBtc = round(getLtc()[0]/getBtc()[0], 4)
  LtcBtc = "#Litecoin: " + "₿" + str(LtcBtc) 
  relativeList.append(LtcBtc)
  LtcBtcPc = round(getLtc()[1]-(getBtc()[1]), 2)
  relativeList.append(LtcBtcPc)

  #Get Bitcoin-Cash
  BchBtc = round(getBch()[0]/getBtc()[0], 4)
  BchBtc = "#BitcoinCash: " + "₿" + str(BchBtc) 
  relativeList.append(BchBtc)
  BchBtcPc = round(getBch()[1]-(getBtc()[1]), 2)
  relativeList.append(BchBtcPc)

  return relativeList



def getCryptoPrices():
  tweetContent = "Price of Top 5 Crypto-Currencies:" + "\n" + formatUSD()[0] + " (" + str(getBtc()[1]) + "%)" + "\n" + formatUSD()[1] +  " (" + str(getEth()[1]) + "%)" + "\n" + formatUSD()[2] + " (" + str(getXrp()[1]) + "%)" + "\n" + formatUSD()[3] + " (" + str(getLtc()[1]) + "%)" + "\n" + formatUSD()[4] + " (" + str(getBch()[1]) + "%)"
  return tweetContent

def getCryptoRelative():
  tweetContent = "#BTC Price of Top Crypto-Currencies:" + "\n" + formatRelative()[0] + " (" + str(formatRelative()[1]) + "%)" + "\n" + formatRelative()[2] + " (" + str(formatRelative()[3]) + "%)" + "\n" + formatRelative()[4] + " (" + str(formatRelative()[5]) + "%)"
  return tweetContent

#print(getCryptoRelative())



def tweetPrices():
  while True:
    print("---CryptoPrices---")
    for i in range(100):
      print(i)
      time.sleep(100) 

    api.update_status(getCryptoPrices()) 
    
    print("---CryptoRelative---")
    for i in range(100):
      print(i)
      time.sleep(100) 

    api.update_status(getCryptoRelative()) 

tweetPrices()
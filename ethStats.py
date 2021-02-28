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

    #Appending Gas Values 
    statsList.append(int(lowFee.contents[0]))
    statsList.append(int(avgFee.contents[0]))
    statsList.append(int(highFee.contents[0]))

    return statsList

getWalletStats()
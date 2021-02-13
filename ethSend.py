from web3 import Web3


w3 = Web3(Web3.HTTPProvider('https://mainnet.infura.io/v3/5d6be6c002c744358836ac43f459d453'))
#print(w3.eth.get_block('latest'))

#Get value of address
#web3.eth.get_balance('0xd3CdA913deB6f67967B99D67aCDFa1712C293601')

#Works! just need a way to automatically get gas price

address='0x122dF7168B01C281E528484a6B392CcB5A6e16D7'

signed_txn = w3.eth.account.signTransaction(dict(
    nonce=w3.eth.getTransactionCount(address),
    gasPrice=w3.eth.gas_price,
    gas=100000,
    to='0x1736200696672FB6aBC7A68b6905001291eCeBd9',
    value=12345,
    data=b'',
  ),
  '0xee9715b9221fd260146e7562dd5fa389fc70f984eac4a0aee22b0f6372384109',
)

print(w3.eth.sendRawTransaction(signed_txn.rawTransaction))



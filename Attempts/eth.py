import os

#Used to create private key and address
from tinyec.ec import SubGroup, Curve
from Crypto.Random.random import randint
from web3 import Web3

#Used to store and encrypt wallet
from Crypto.Cipher import AES
from Crypto.Protocol.KDF import scrypt
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes
import json

#def createWallet(password):
p = int("FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEFFFFFC2F", 16)
n = int("FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEBAAEDCE6AF48A03BBFD25E8CD0364141", 16)
h = 1

x = int("79BE667EF9DCBBAC55A06295CE870B07029BFCDB2DCE28D959F2815B16F81798", 16)
y = int("483ADA7726A3C4655DA4FBFC0E1108A8FD17B448A68554199C47D08FFB10D4B8", 16)
g = (x,y)

field = SubGroup(p, g, n, h)
curve = Curve(a = 0, b = 7, field = field, name = 'secp256k1')
private_key = 0x60cf347dbc59d31c1358c8e5cf5e45b822ab85b79cb32a9f3d98184779a9efc2
public_key = private_key * curve.g

public_key_hex = hex(public_key.x)[2:] + hex(public_key.y)[2:]
print(public_key_hex)


address = Web3.keccak(hexstr = public_key_hex).hex()
address = "0x" + address[-40:]
address = Web3.toChecksumAddress(address)
#return private_key, address
print(address)
"""
	salt = get_random_bytes(16)

	key = scrypt(password, salt, 32, N = 2**20, r = 8, p = 1)

	private_key = Web3.toHex(private_key)[2:]
	data = str(private_key).encode('utf-8')

	cipher = AES.new(key, AES.MODE_CBC)
	ct_bytes = cipher.encrypt(pad(data, AES.block_size))

	salt = salt.hex()
	iv = cipher.iv.hex()
	ct = ct_bytes.hex()

	output = {"salt" : salt, "initialization vector" : iv, "encrypted private key" : ct}

	with open("wallets/" + address + '.txt', 'w') as json_file:
		json.dump(output, json_file)


#Used to Decode the ethereum Wallet
def decodeWallet(password, address):
	with open("wallets/" + address) as f:
		data = json.load(f)

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
		print(pt.decode('utf-8'))
		
	except:
		print("wrong password entered")


startInput = input("1: Create a Wallet, 2: Open a Wallet")

if(startInput == "1"):
	inputPassword = input("Please type a memorable password")
	inputPassword = bytes(inputPassword, 'utf-8')
	createWallet(inputPassword)

elif(startInput == "2"):
	inputPassword = input("Please type your wallets password")
	inputPassword = bytes(inputPassword, 'utf-8')
	wallet_files = os.listdir("wallets/")
	decodeWallet(inputPassword, wallet_files[0])
"""

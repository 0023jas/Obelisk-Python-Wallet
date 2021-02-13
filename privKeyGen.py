from random import randint

def genPrivKey():
  N=int("FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEBAAEDCE6AF48A03BBFD25E8CD0364141", 16)
  private_key = randint(1, N)
  return private_key

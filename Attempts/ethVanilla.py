from random import randint
import math
#Generate Private Key
"""
lastWallet = int("FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEBAAEDCE6AF48A03BBFD25E8CD0364141", 16)
private_key = randint(1, lastWallet)
private_key = hex(private_key)

print(private_key)
"""
"""
#Important Variables
#Pcurve, for proven prime
Pcurve = 2**256 - 2**32 - 2**9 - 2**8 - 2**7 - 2**6 - 2**4 - 1
#Number of possible wallets
N = 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEBAAEDCE6AF48A03BBFD25E8CD0364141
#Points for the Curve Function
Acurve = 0
Bcurve = 7
#X and Y coordinates for starting points
Gx = 55066263022277343669578718895168534326250603453777594175500187360389116729240
Gy = 32670510020758816978083085130507043184471273380659243275938904335757337482424
Gpoint = (Gx, Gy)
privKey = 0xA0DC65FFCA799873CBEA0AC274015B9526505DAAAED385155425F7337704883E

def modinv(a,n=Pcurve): #Extended Euclidean Algorithm/Division in elliptic curves
  lm = 1
  hm = 0
  low = a%n
  high = n
  while low > 1:
    ratio = high/low
    nm = hm-lm*ratio
    new = high-low*ratio
    lm = nm
    low = new
    hm = lm
    high = low
    
  return lm%n

def ECadd(a,b): #Not actually addition just invented for EC
  lamAdd = ((b[1]-a[1]) * modinv(b[0]-a[0], Pcurve)) % Pcurve
  x = (lamAdd*lamAdd-a[0]-b[0]) % Pcurve
  y = (lamAdd*(a[0]-x)-a[1]) % Pcurve
  return (x,y)

def ECdouble(a): #Point Doubling, also invented for EC
  lam = ((3*a[0]*a[0]+Acurve) * modinv((2*a[1]),Pcurve)) % Pcurve
  x = (lam*lam-2*a[0]) % Pcurve
  y = (lam*(a[0]-x)-a[1]) % Pcurve
  return (x,y)

def EccMultiply(GenPoint, ScalarHex): #Double and Add. Not true multiplication
  if ScalarHex == 0 or ScalarHex >= N: 
    return "Invalid Private Key"
  
  ScalarBin = str(bin(ScalarHex))[2:]
  Q=GenPoint
  for i in range(1,len(ScalarBin)): # This is the EC multiplication
    Q=ECdouble(Q)
    if ScalarBin[i] == "1":
      Q=ECadd(Q, GenPoint)
  return Q
"""

Pcurve = 2**256 - 2**32 - 2**9 - 2**8 - 2**7 - 2**6 - 2**4 - 1 # The proven prime
N=int("FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEBAAEDCE6AF48A03BBFD25E8CD0364141", 16) # Number of points in the field
Acurve = 0; Bcurve = 7 # These two defines the elliptic curve. y^2 = x^3 + Acurve * x + Bcurve
Gx = int("79BE667EF9DCBBAC55A06295CE870B07029BFCDB2DCE28D959F2815B16F81798", 16)
Gy = int("483ADA7726A3C4655DA4FBFC0E1108A8FD17B448A68554199C47D08FFB10D4B8", 16)
GPoint = (Gx,Gy) # This is our generator point. Trillions of dif ones possible

#Individual Transaction/Personal Information
privKey = int("A0DC65FFCA799873CBEA0AC274015B9526505DAAAED385155425F7337704883E", 16) #replace with any private key

def modinv(a,n=Pcurve): #Extended Euclidean Algorithm/Division in elliptic curves
  lm = 1
  hm = 0
  low = a%n
  high = n
  while low > 1:
    ratio = high/low
    nm = hm-lm*ratio
    new = high-low*ratio
    lm = nm
    low = new
    hm = lm
    high = low
    
  return lm%n

def ECadd(a,b): # Not true addition, invented for EC. Could have been called anything.
  LamAdd = ((b[1]-a[1]) * modinv(b[0]-a[0],Pcurve)) % Pcurve
  x = (LamAdd*LamAdd-a[0]-b[0]) % Pcurve
  y = (LamAdd*(a[0]-x)-a[1]) % Pcurve
  return (x,y)

def ECdouble(a): # This is called point doubling, also invented for EC.
  Lam = ((3*a[0]*a[0]+Acurve) * modinv((2*a[1]),Pcurve)) % Pcurve
  x = (Lam*Lam-2*a[0]) % Pcurve
  y = (Lam*(a[0]-x)-a[1]) % Pcurve
  return (x,y)

def EccMultiply(GenPoint,ScalarHex): #Double & add. Not true multiplication
  ScalarBin = str(bin(ScalarHex))
  Q=GenPoint
  for i in range(1, len(ScalarBin)): # This is invented EC multiplication.
    Q=ECdouble(Q); # print "DUB", Q[0]; print
    if ScalarBin[i] == "1":
      Q=ECadd(Q,GenPoint); # print "ADD", Q[0]; print
  return (Q)

PublicKey = EccMultiply(GPoint,privKey)   
print(int(PublicKey[1]))


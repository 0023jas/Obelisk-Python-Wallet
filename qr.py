import qrcode

#Takes in Address, Saves QR in /qr 
def qrGenerate(inputAddress):
    addressName = inputAddress
    img = qrcode.make(addressName)
    img.save("qr/" + addressName + '.png')
    return addressName

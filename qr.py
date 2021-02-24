import qrcode

def qrGenerate(inputAddress):
    addressName = inputAddress
    img = qrcode.make(addressName)
    img.save("qr/" + addressName + '.png')
    return addressName

qrGenerate('0x6cAcb8266Ad0E8a769B05517B35cd6fba0551c31')
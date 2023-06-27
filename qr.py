import qrcode as qr
url = input("Enter the url or anything else to make a qr : ")
keyname = input("Enter a keyname for your qr : ")
img = qr.make(url)
img.save(str(keyname)+".png")
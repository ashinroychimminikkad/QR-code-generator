import qrcode
from pyzbar.pyzbar import decode
from PIL import Image

#this is the code for qrcode generator
myqr = qrcode.make("https://www.linkedin.com/in/ashin-roy-595375253/")

myqr.save("myqr.png")


# the code for qr code decoder

QR = decode(Image.open("myqr.png"))
print(QR[0].data.decode("ascii"))

import qrcode
import tkinter as tk
from tkinter import filedialog
from tkinter import Tk
from pyzbar.pyzbar import decode
from PIL import Image


#this is the code for qrcode generator
url = input("enter the content you want to convert to qr code:")

qrcod = qrcode.make(url)
qrcod.save("myqr.png")


# the code for qr code decoder

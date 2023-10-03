import pyqrcode

url = input("Enter url to generate code: ")

qr_code = pyqrcode.create(url)
qr_code.svg('qrcode.svg', scale=8)

import pyqrcode

url = input('Enter URL to generate QR code: ')

qr = pyqrcode.create(url)
qr.svg('qr.svg',8)

qr.eps('qr.eps', scale=2)
print(qr.terminal(quiet_zone=1))
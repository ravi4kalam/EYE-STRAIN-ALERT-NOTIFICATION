import pyqrcode
import png
from pyqrcode import QRCode

s=''' import pyqrcode
import png
from pyqrcode import QRCode

s="https://www.python.org/" #enter text
qcode=pyqrcode.create(s)
qcode.svg("Linkedin.svg ",scale=8)
qcode.png("Linkedin.png",scale=13)''' #enter text
qcode=pyqrcode.create(s)
qcode.svg("QRprogram.svg ",scale=8)
qcode.png("QRprogram.png",scale=6)
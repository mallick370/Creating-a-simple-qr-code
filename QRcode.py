# -*- coding: utf-8 -*-
"""
Created on Wed Mar  6 14:02:33 2019

@author: KIIT
"""

import pyqrcode
from pyqrcode import QRCode

s=input("Enter your name\n")
#s="https://github.com/mallick370"
url=pyqrcode.create(s)
url.svg("myqr.svg",scale=8)
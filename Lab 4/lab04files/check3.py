# -*- coding: utf-8 -*-
"""
Created on Wed Oct  6 14:06:35 2021

@author: User
"""

from PIL import Image

im = Image.new('RGB', (1000, 360), 'white')
im1 = Image.open('1.jpg')
im2 = Image.open('2.jpg')
im3 = Image.open('3.jpg')
im4 = Image.open('4.jpg')
im5 = Image.open('5.jpg')
im6 = Image.open('6.jpg')

im1 = im1.resize((im1.size[0] // 2, 256))
im2 = im2.resize((im2.size[0] // 2, 256))
im3 = im3.resize((im3.size[0] // 2, 256))
im4 = im4.resize((im4.size[0] // 2, 256))
im5 = im5.resize((im5.size[0] // 2, 256))
im6 = im6.resize((im6.size[0] // 2, 256))

x1 = 31
im.paste(im1, (x1, 20))
x2 = x1 + im1.size[0] + 10
im.paste(im2, (x2, 60))
x3 = x2 + im2.size[0] + 10
im.paste(im3, (x3, 20))
x4 = x3 + im3.size[0] + 10
im.paste(im4, (x4, 60))
x5 = x4 + im4.size[0] + 10
im.paste(im5, (x5, 20))
x6 = x5 + im5.size[0] + 10
im.paste(im6, (x6, 60))

im.show()
# -*- coding: utf-8 -*-
"""
Created on Tue Oct  5 15:17:47 2021

@author: User
"""

from PIL import Image
im = Image.new('RGB', (512, 512), 'white')
im2 = Image.open('ca.jpg')
im3 = Image.open('im.jpg')
im4 = Image.open('hk.jpg')
im5 = Image.open('bw.jpg')

im2 = im2.resize((256, 256))
im3 = im3.resize((256, 256))
im4 = im4.resize((256, 256))
im5 = im5.resize((256, 256))

im.paste(im2, (0, 0))
im.paste(im3, (256, 0))
im.paste(im4, (0, 256))
im.paste(im5, (256, 256))
im.show()
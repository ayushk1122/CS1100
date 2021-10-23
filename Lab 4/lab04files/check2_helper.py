# -*- coding: utf-8 -*-
"""
Created on Tue Oct  5 15:34:04 2021

@author: User
"""

from PIL import Image

def make_square (image) :
    width = image.size[0]
    height = image.size[1]
    if (width > height) :
        im_crop = image.crop((0, 0, (width - (width - height)), height))
    elif (height > width) :
        im_crop = image.crop((0, 0, width, (height - (height - width))))
    else :
        im_crop = image.crop((0, 0, width, height))
    return im_crop

    
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 14 21:31:29 2021
Ayush Krishnappa 
This program creates a framed box around the dimensions inputted by a user of a
designated charachter the user inputs
Prof Turner CS 1100
@author: User
"""

input_char = input("Enter frame character ==> ")
print(input_char)

height = input("Height of box ==> ")
print(height)

width = input("Width of box ==> ")
print(width + "\n")

print("Box:")

frame = input_char * int(width)
height = int(height)
width = int(width)
gap = int(width - 2)
row = input_char + (gap * " ") + input_char + "\n"

dimensions = str(width) + "x" + str(height) 
dim_length = len(dimensions)

gap_left = int((gap - dim_length) / 2)
gap_right = int(gap - (gap_left + dim_length))

border_top = int((height - 3) / 2)
border_bottom = int((height / 2) - 1)

print(frame)
print(row * border_top, end = "")
print(input_char + (" " * gap_left) + dimensions + (" " * gap_right) + input_char)
print(row * border_bottom, end = "")
print(frame)




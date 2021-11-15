# -*- coding: utf-8 -*-
"""
Created on Tue Oct 26 14:22:16 2021

@author: Ayush
"""

line = input("Enter a line of text to be parsed: ")

def parse_line (text):
    if (text.count('/') < 3):
        return 'None'
    output = []
    split = text.rsplit('/', 3)
    if ((split[len(split) - 1].isdigit() == False) or (split[len(split) - 2].isdigit() == False) or (split[len(split) - 3].isdigit() == False)):
        return 'None'
    for string in split:
        if (string.isdigit()):
            output.append(int(string))
    
    output.append(split[0])
    return output
    
    
print(parse_line(line))
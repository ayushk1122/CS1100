# -*- coding: utf-8 -*-
"""
Created on Tue Oct 26 15:22:12 2021

@author: Ayush
"""

def get_line (fname, parno, lineno):
    f = open(fname + '.txt', encoding = 'utf8')
    s = f.read()
    paras = s.split('\n\n')
    paragraph = paras[parno - 1]
    
    lines = paragraph.split('\n')
    
    for value in lines:
        if (value == ''):
            lines.remove(value)
    
    line = lines[lineno - 1]
    return line

file_num = input("Please enter the file number ==> ")
para_num = int(input("Please enter the paragraph number ==> "))
line_num = int(input("Please enter the line number ==> "))
print(get_line(file_num, para_num, line_num))

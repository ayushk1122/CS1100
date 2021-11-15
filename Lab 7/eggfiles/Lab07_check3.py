# -*- coding: utf-8 -*-
"""
Created on Wed Oct 27 10:27:37 2021

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
o_file = input("Enter the name of an output file: ")

f_out = open(o_file, 'w')

line = get_line(file_num, para_num, line_num)
while (line != 'END/0/0/0'):
    if (get_line(file_num, para_num, line_num).count('/') >= 3):
        line2 = line.rsplit('/', 3)
        f_out.write(line2[0] + '\n')
        file_num = (line2[len(line2) - 3])
        para_num = int(line2[len(line2) - 2])
        line_num = int(line2[len(line2) - 1])
        line = get_line(file_num, para_num, line_num)
    else:
        ##print('Starting location given is incorrect')
        break
    
f_out.close()
    


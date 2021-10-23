# -*- coding: utf-8 -*-
"""
Created on Tue Oct 19 10:06:39 2021

@author: Ayush
"""
output = ''
grid = [[0 for i in range(9)] for j in range (9)]

for i in range (9):
    for j in range (9):
        if (j % 3 == 0):
            output += ' '
        output += (str(i) + ',' + str(j) + ' ')
        grid[i][j] = (i, j)
    output += '\n'
    if ((i + 1) % 3 == 0 and i != 0):
        output += '\n'
    
print(output)

outputr = ''
row = 2

for i in range (len(grid[row])):
    outputr += (str(grid[row][i]) + ' ')
    
print(outputr)

outputc = ''
col = 5

for i in range (len(grid[0])):
    outputc += (str(grid[i][col]) + ' ')
    
print(outputc)
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 19 11:06:36 2021

@author: Ayush
"""

row = int(input("Enter a row index starting at 0: ").strip())
column = int(input("Enter a column index starting at 0: ").strip())
num = int(input("Enter a number to input into the sodoku board: "))


bd = [ [ '1', '.', '.', '.', '2', '.', '.', '3', '7'],
       [ '.', '6', '.', '.', '.', '5', '1', '4', '.'],
       [ '.', '5', '.', '.', '.', '.', '.', '2', '9'],
       [ '.', '.', '.', '9', '.', '.', '4', '.', '.'],
       [ '.', '.', '4', '1', '.', '3', '7', '.', '.'],
       [ '.', '.', '1', '.', '.', '4', '.', '.', '.'],
       [ '4', '3', '.', '.', '.', '.', '.', '1', '.'],
       [ '.', '1', '7', '5', '.', '.', '.', '8', '.'],
       [ '2', '8', '.', '.', '4', '.', '.', '.', '6'] ]

def ok_to_add (row, column, num, grid):
    while (row < 0 or row >= len(grid)):
        row = int(input("Enter a row index starting at 0: ").strip())
    while (column < 0 or column >= len(grid[0])):
        column = int(input("Enter a column index starting at 0: ").strip())
    while (num < 0):
        num = int(input("Enter a number to input into the sodoku board: "))
    
    
    for i in range(len(grid)):
        if (str(grid[row][i]) == str(num)):
            return False
        
            
    for i in range(len(grid[row])):
        if (str(grid[i][column]) == str(num)):
            return False
            
    grid_x = (row // 3) * 3
    grid_x_loop = grid_x + 3
    grid_y = (column // 3) * 3
    grid_y_loop = grid_y + 3
    
    while (grid_x < grid_x_loop):
        grid_y = (column // 3) * 3
        while (grid_y < grid_y_loop):
            if (grid[grid_x][grid_y] == str(num)):
                return False
            grid_y += 1
        grid_x += 1
        
    stop = False
    for i in range (len(grid)):
        for j in range (len(grid[0])):
            if (i == row and j == column):
                grid[i][j] = str(num)
                stop = True
                break
        if (stop):
            break
    
    print_sodoku(grid)
                
    return True

def print_sodoku (grid):
        
    sodoku = ''

    sodoku += ('-' * 25 + '\n')
    for i in range (len(grid)):
        for j in range (len(grid[0]) + 1):
            if (j % 3 == 0):
                if (j != 9):
                    sodoku += ('|' + ' ')
                else:
                    sodoku += '|'
            if (j < len(grid[0])):
                sodoku += (str(grid[i][j]) + ' ')
        sodoku += '\n'
        if ((i + 1) % 3 == 0):
            sodoku += ('-' * 25 + '\n')
            
    print(sodoku)



if (ok_to_add(row, column, num, bd) == False):
    print("This number cannot be added")
else:  
    ok_to_add(row, column, num, bd)


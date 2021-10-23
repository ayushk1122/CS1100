# -*- coding: utf-8 -*-
"""
Created on Wed Oct 20 14:09:48 2021

@author: Ayush
"""

import lab06_util

file = input("Enter a file name with a soduku board: ")
file = file.strip()

board = lab06_util.read_sudoku(file)

def ok_to_add (row, column, num, grid):
    while (int(row) < 0 or int(row) >= len(grid)):
        row = int(input("Enter a row index starting at 0: ").strip())
    while (int(column) < 0 or int(column) >= len(grid[0])):
        column = int(input("Enter a column index starting at 0: ").strip())
    while (int(num) < 0):
        num = int(input("Enter a number to input into the sodoku board: "))
    
    
    for i in range(len(grid)):
        if (str(grid[row][i]) == str(num) and (i != column)):
            return False
        
            
    for i in range(len(grid)):
        if (str(grid[i][column]) == str(num) and (i != row)):
            return False
    
    """
    grid_x = (row // 3) * 3
    grid_x_loop = grid_x + 3
    grid_y = (column // 3) * 3
    grid_y_loop = grid_y + 3
    
    while (grid_x < grid_x_loop):
        grid_y = (column // 3) * 3
        while (grid_y < grid_y_loop):
            if (grid[grid_x][grid_y] == str(num) and (grid_x != row) and (grid_y != column)):
                return False
            grid_y += 1
        grid_x += 1
    """
    
    return True

def print_sodoku (grid, row, column, num):     
    stop = False
    for i in range (len(grid)):
        for j in range (len(grid[0])):
            if (i == row and j == column):
                grid[i][j] = str(num)
                stop = True
                break
        if (stop):
            break
    return grid
    
def verify_board (board): 
    for i in range (len(board)):
        for j in range (len(board[0])):
            if (board[i][j] == '.' or (ok_to_add(i, j, board[i][j], board) == False)):
                return False
    return True


while (verify_board(board) == False):
    print("The solution for the given board is not valid, please input values to complete it.")
    row = int(input("Enter a row index starting at 0: ").strip())
    column = int(input("Enter a column index starting at 0: ").strip())
    num = int(input("Enter a number to input into the sodoku board: "))
    
    while (row < 0 or row >= len(board)):
        row = int(input("Enter a row index starting at 0: ").strip())
    while (column < 0 or column >= len(board[0])):
        column = int(input("Enter a column index starting at 0: ").strip())
    while (num < 0):
        num = int(input("Enter a number to input into the sodoku board: "))
        
    if (ok_to_add(row, column, num, board)):
        board = print_sodoku(board, row, column, num)
        
print("Sodoku Board is solved!")
sodoku = ''

sodoku += ('-' * 25 + '\n')
for i in range (len(board)):
    for j in range (len(board[0]) + 1):
        if (j % 3 == 0):
            if (j != 9):
                sodoku += ('|' + ' ')
            else:
                sodoku += '|'
        if (j < len(board[0])):
            sodoku += (str(board[i][j]) + ' ')
    sodoku += '\n'
    if ((i + 1) % 3 == 0):
        sodoku += ('-' * 25 + '\n')
        
print(sodoku)


            
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 15 10:13:46 2021
This program takes data from a file with a list of grids and outputs certain
characteristics of a user specified grid.
This program uses multiple different types of loops, conditionals, functions, and
print statements to accomplish its task
@author: Ayush Krishnappa
"""

import hw5_util

num_grids = hw5_util.num_grids()

grid_num = input("Enter a grid index less than or equal to " + str(num_grids) + " (0 to end): ")
print(grid_num)
grid_num = int(grid_num)

## checks if the inputted grid index is a valid one and loops until valid one is given
while (grid_num < 1 or grid_num > num_grids):   
    grid_num = input("Enter a grid index less than or equal to " + str(num_grids) + " (0 to end): ")
    print(grid_num)
    grid_num = int(grid_num)
    
grid_print = input("Should the grid be printed (Y or N): ")
print(grid_print)

    
"""
This function takes a row column index along with the number of rows and columns in a grid
and output a list of neighbors for that (row, column) value

"""
def get_nbrs (row, col, num_rows, num_cols):
    ## uses calculations given to calculate neighbors for the specified value
    neighbor0 = (max(row - 1, 0), col)
    neighbor1 = (row, max(col - 1, 0))
    neighbor2 = (row, min(col + 1, num_cols - 1))
    neighbor3 = (min(row + 1, num_rows - 1), col)
    neighbors = []

    ## checks to make sure neighbor values aren't identical to original value
    ## then adds the neighbor value to the end of the list
    if (neighbor0 != (row, col)): neighbors.append(neighbor0)
    if (neighbor1 != (row, col)): neighbors.append(neighbor1)
    if (neighbor2 != (row, col)): neighbors.append(neighbor2)
    if (neighbor3 != (row, col)): neighbors.append(neighbor3)
    
    return neighbors

"""
This function takes a grid index as the input and prints if the suggested path
is a valid one or not
Also calculates and prints the downaward and upward elevation values for the given path
"""
def path (n):
    grid_n = hw5_util.get_grid(n)
    sug_path = hw5_util.get_path(n)
    downward = 0
    upward = 0
    ## boolean value to keep track of if the path is valid or not
    valid_path = False
    
    ## loops through each index of the sugggested path 
    for i in range(len(sug_path) - 1):
        ## resets the path boolean value to false to check each iteration of the 
        ## suggested path to make sure it is still valid
        valid_path = False
        ## loops through each neighbor in the list of neighbors for each 
        ## individual value in the suggested path
        ## essentially calculates the neighbors for each suggested path value each iteration
        for neighbor in get_nbrs(sug_path[i][0], sug_path[i][1], len(grid_n), len(grid_n[0])):
            ## checks that the index after each value is a neighbor of the prior
            if (sug_path[i+1] == neighbor):
                valid_path = True
                ## conditonal block to chekc if the path is downward of upward elevation
                if (grid_n[sug_path[i][0]][sug_path[i][1]] > grid_n[sug_path[i+1][0]][sug_path[i+1][1]]):
                    downward += (grid_n[sug_path[i][0]][sug_path[i][1]] - grid_n[sug_path[i+1][0]][sug_path[i+1][1]])
                elif (grid_n[sug_path[i][0]][sug_path[i][1]] < grid_n[sug_path[i+1][0]][sug_path[i+1][1]]):
                    upward += (grid_n[sug_path[i+1][0]][sug_path[i+1][1]] - grid_n[sug_path[i][0]][sug_path[i][1]])
        ## if the valid path is false after entire loop prints the invalid step of the current
        ## loop iteration indexes
        if (valid_path == False):
            print("Path: invalid step from {} to {}".format(sug_path[i], sug_path[i+1]))
            break
    ## otherwise prints the required stats for a valid path
    if (valid_path):
        print("Valid path")
        print("Downward", downward)
        print("Upward", upward)
    
    
"""
This functon takes the start locations for a given grid number and the grid index
and prints neighbors for each start location value
"""
def print_nbrs (start_loc, n):
    grid_n = hw5_util.get_grid(n)
    output = ''
    
    ## loops through each location in the start location list
    for loc in start_loc:
        output += ('Neighbors of {}: '.format(loc))
        
        ## loops through each neighbor in the list of neihbors for the specified 
        ## location in the start location list
        for neighbor in get_nbrs(loc[0], loc[1], len(grid_n), len(grid_n[0])):
            length = len(get_nbrs(loc[0], loc[1], len(grid_n), len(grid_n[0])))
            ##conditionals to make sure a space isn't printed after the last value
            if (neighbor != get_nbrs(loc[0], loc[1], len(grid_n), len(grid_n[0]))[length - 1]):
                output += (str(neighbor) + ' ')
            else: 
                output += (str(neighbor))
        ## conditional to make sure a new line isn't printed after the last value
        if (loc != start_loc[len(start_loc) - 1]):
            output += '\n'
    print(output)
    
"""
This function takes the user inputted decision to print or not and the grid index
and output the printed grid in a formatted fashion
"""
def print_grid (print_yn, n):
    grid_n = hw5_util.get_grid(n)
    print_yn = print_yn.lower()
    output = ''
    if (print_yn == 'y'):
        print("Grid", n)
        
        ## loops through grid rows
        for i in range (len(grid_n)):
            ## loops through grid columns
            for j in range (len(grid_n[0])):
                ## formats spaces based off number of digits in the number
                if (grid_n[i][j] >= 10): output += (2 * ' ' + str(grid_n[i][j]))
                elif (grid_n[i][j] < 10): output += (3 * ' ' + str(grid_n[i][j]))
                elif (grid_n[i][j] > 100): output += (str(grid_n[i][j]))
            ## conditional to make sure a new line isn't added at the end
            if (i != (len(grid_n) - 1)):
                output += '\n'
        print(output)
    print("Grid has {} rows and {} columns".format(len(grid_n), len(grid_n[0])))
                
## method calls for the specified grid index, and decision to print
print_grid(grid_print, grid_num)     
start_loc = hw5_util.get_start_locations(grid_num) 
print_nbrs(start_loc, grid_num)
path(grid_num)

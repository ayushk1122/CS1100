# -*- coding: utf-8 -*-
"""
Created on Fri Oct 15 10:13:46 2021
This program takes data from a file with a list of grids and outputs a set of paths
from each starting location (gradual and steep) and returns if this path reaches
a global maximum of the data set, a local maximum, or no maximum.
Also prints a grid if the user wants it, which specifies how many of the coordinates are
included in the paths.
This program uses functions, multiple different loops, conditionals, and inputs to complete
its task
@author: Ayush Krishnappa
"""

import hw5_util

num_grids = hw5_util.num_grids()


grid_num = input("Enter a grid index less than or equal to " + str(num_grids) + " (0 to end): ")
print(grid_num)
grid_num = int(grid_num)

max_step = input("Enter the maximum step height: ")
print(max_step)
max_step = int(max_step)

## checks if the inputted grid index is a valid one and loops until valid one is given
while (grid_num < 1 or grid_num > num_grids):   
    grid_num = input("Enter a grid index less than or equal to " + str(num_grids) + " (0 to end): ")
    print(grid_num)
    grid_num = int(grid_num)
    
grid_print = input("Should the path grid be printed (Y or N): ")
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
This function takes an index for a grid and returns the global max value of the specified
grid
"""
def find_max (n):
    grid_n = hw5_util.get_grid(n)
    global_max = 0
    global_max_cor = (0, 0)

    for i in range (len(grid_n)):
        for j in range (len(grid_n[0])):
            if (grid_n[i][j] > global_max):
                global_max = grid_n[i][j]
                global_max_cor = (i, j)
        
    return global_max_cor

"""
This function takes a grid index and a row index and returns the local max value of
the specified row 
"""
def find_local_max (n, row):
    grid_n = hw5_util.get_grid(n)
    local_max = 0
    local_max_cor = (0, 0)
    
    for i in range (len(grid_n[row])):
        if (grid_n[row][i] > local_max):
            local_max = grid_n[row][i]
            local_max_cor = (row, i)

    return local_max_cor

"""
This function takes a starting location, grid index, and yser inputted max step value,
and returns the steepest path in the form of a list of tuples
"""
def steepest_path (start_loc, n, max_step):
    grid_n = hw5_util.get_grid(n)
    path = []
    path.append(start_loc)
    ## step variable to keep track of the current difference
    step = 0
    ## index variable to track if there any more available moves in the path
    index = 0
    ## difference variable to store the max difference
    diff = 0
    ## temp neighbor variable to keep track of the current position of the path
    neighbor_temp = (0, 0)
    while (True):
        index = 0
        step = 0
        ## gets the set of neighbors for the start location
        neighbors = get_nbrs(start_loc[0], start_loc[1], len(grid_n), len(grid_n[0]))
        ## loops through each neighbor to compare to start location
        for neighbor in neighbors:
           diff = (grid_n[neighbor[0]][neighbor[1]]) - (grid_n[start_loc[0]][start_loc[1]])
           ## makes sure the difference is valid according to the rules of being positive
           ## and less than the user inputted max step
           if (diff > 0 and diff <= max_step):
               ## makes sure max difference is being stored
               if (diff > step):
                   step = diff
                   ## updates current position of the path
                   neighbor_temp = neighbor
           else: 
               ## increments index if no neighbor is not a valid path
               index += 1
        
        ## checks if any neighbors were valid, if none are valid paths index will
        ## be equal to the number of neighbors and therefore end the loop
        if (index == len(neighbors)):
            break
        
        path.append(neighbor_temp)
        ## updates start location to the neighbor position to continue path
        start_loc = neighbor_temp
        
    return path

"""
This function takes the start location, grid index, and max step as its inputs and
returns the gradual path in the form of a list of tuples
This function uses the same logic as steepest path but finds the minimum difference instead
"""
def gradual_path (start_loc, n, max_step):
    grid_n = hw5_util.get_grid(n)
    path = []
    path.append(start_loc)
    index = 0
    ## max value step to find minimum difference
    step = 10000
    diff = 0
    neighbor_temp = (0, 0)
    while (True):
        index = 0
        step = 10000
        neighbors = get_nbrs(start_loc[0], start_loc[1], len(grid_n), len(grid_n[0]))
        for neighbor in neighbors:
            diff = (grid_n[neighbor[0]][neighbor[1]]) - (grid_n[start_loc[0]][start_loc[1]])
            if (diff > 0 and diff <= max_step):
                ## makes sure minimum differenc is being stored
                if (diff < step):
                    step = diff
                    neighbor_temp = neighbor
            else:
                index += 1
        
        if (index == len(neighbors)):
            break
        
        path.append(neighbor_temp)
        start_loc = neighbor_temp
        
    return path

"""
This function takes the path, the type of path, and grid index as inputs
and prints the resulting path in the correct format
"""
def print_path (path, tpath, n):
    output = ''
    ## tpath is the string of either steep or gradual 
    output += (tpath)
    for i in range (len(path)):
        ## uses modulus 5 to make sure only 5 coordinates are printed on each line
        if (i % 5 == 0 and i != 0):
            output += '\n'
            output += (str(path[i]) + ' ')
        else:
            ## conditional block to make sure spaces aren't printed after last element
            if (i != len(path)):
                output += (str(path[i]) + ' ')
            else: 
                output += (str(path[i]))
    ## adds the type of maximum the path reaches using the max_type function
    output += ('\n' + max_type(path, n))
    
    return output
    
"""
This function takes the path and grid index as inputs and returns the type of 
maximum the path reaches in the form of the correct string 
Uses the find_max and find_local_max functions to determine the correct
corresponding string
"""
def max_type (path, n):
    grid_n = hw5_util.get_grid(n)
    loc_max = find_local_max(n, path[len(path) - 1][0])
    mtype = ''
    if (path[len(path) - 1] == find_max(n)):
        mtype = 'global maximum'
    ## checks if local max is greater than all neighbors and greater than all values in row
    elif (path[len(path) - 1] == loc_max):
        neighbors = get_nbrs(loc_max[0], loc_max[1], len(grid_n), len(grid_n[0]))
        ## count variable to keep track of how many neighbors loc max is greater then
        count = 0
        for neighbor in neighbors:
            if (grid_n[loc_max[0]][loc_max[1]] > grid_n[neighbor[0]][neighbor[1]]):
                count += 1

        ## if the count is equal to the length of the neighbors list
        ## that means the local max is greater than all neighbors as well
        if (count == len(neighbors)):
            mtype = 'local maximum'
        else:
            mtype = 'no maximum'
            
    else: 
        mtype = 'no maximum'
        
    return mtype
            
"""
This function takes the steepest paths, gradual paths, and print decision from the user
as inputs and prints the corresponding grid of coordinate counts that occur in both of the
paths
Both the steepest path and gradual path are list of lists of all the paths of all 
starting locations
"""
def path_grid (spath, gpath, n, print_yn):
    print_yn = print_yn.lower()
    ## total count for coordinate occurances in each path
    count = 0
    if (print_yn == 'y'):
        grid_n = hw5_util.get_grid(n)
        for i in range (len(grid_n)):
            count = 0
            for j in range (len(grid_n[0])):
                ## two for each loops to loop through the two different paths
                ## and counts the number of times a coordinate occurs in both paths
                for path in spath:
                    count += path.count((i, j))
                for path in gpath:
                    count += path.count((i, j))
                grid_n[i][j] = count
                ## resets the count to 0 since loops through a different path each time
                count = 0
                
        return grid_n
    
"""
This function takes the path grid as input and returns a string of the formatted output
of how the grid should be printed
"""
def print_path_grid (path_grid):
    output = 'Path grid\n'
    for i in range (len(path_grid)):
        for j in range (len(path_grid[0])):
            ## if the value is equal to 0, a . is printed instead as specified by the spec
            if (path_grid[i][j] == 0):
                ## conditional block to make sure space isn't printed before first value
                if (j != len(path_grid[0])):
                    output += (2 * ' ' + '.')
                else:
                    output += '.'
            else:
                if (j != len(path_grid[0])):
                    output += (2 * ' ' + str(path_grid[i][j]))
                else:
                    output += str(path_grid[i][j])
        if (i != len(path_grid) - 1):
            output += '\n'
    return output
                    
    
                
        
## prints the global maximum value and coordinates as specified in the correct format
grid_n = hw5_util.get_grid(grid_num)
print("Grid has {} rows and {} columns".format(len(grid_n), len(grid_n[0])))
print("global max: {} {}".format(find_max(grid_num), grid_n[find_max(grid_num)[0]][find_max(grid_num)[1]]))
print("===")


start_loc = hw5_util.get_start_locations(grid_num) 
output1 = 'steepest path\n'
output2 = 'most gradual path\n'
## total path values, used for the path_grid method 
spath_total = []
gpath_total = []
for loc in start_loc:
    spath = steepest_path(loc, grid_num, max_step)
    ## appends each steep path to the total path list to more easily count occurences
    ## for the path grid
    spath_total.append(spath)
    print(print_path(spath, output1, grid_num) + '\n' + '...')
    gpath = gradual_path(loc, grid_num, max_step)
    gpath_total.append(gpath)
    print(print_path(gpath, output2, grid_num) + '\n' + '===')

## prints the final path grid fully formatted 
print(print_path_grid(path_grid(spath_total, gpath_total, grid_num, grid_print)))


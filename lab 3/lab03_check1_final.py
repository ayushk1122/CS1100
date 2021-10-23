"""
This program experiments with the use of functions
and also learning error checking.


"""

import math

## Function returns the length of a line 
## starting at (x1,y1) and ending at (x2,y2)
def line_length(x1,y1,x2,y2):
    length = (x1-x2)**2 + (y1-y2)**2
    length = math.sqrt(length)
    return length

next_x = input("The next x value ==> ")
next_x = float(next_x)    
next_y = input("The next y value ==> ")
next_y = float(next_y)

initial_x = 10
initial_y = 10

len = line_length(initial_x, initial_y, next_x, next_y)

print("The line has moved from ({:d},{:d}) to ({:d},{:d})".format(initial_x, initial_y, int(next_x), int(next_y)))
    ##"to", str(next_x), + ",", next_y)

print("Total length traveled is: {:0.2f}".format(len))



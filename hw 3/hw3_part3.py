# -*- coding: utf-8 -*-
"""
Created on Mon Oct  4 20:58:37 2021
This program calculates the next 10 yeara worth of bear, berry, and tourists populations given
a current years values. This program uses loops, lists, and a given formulas to calculate new year values.
It also calculates the max and min value of each category. 
@author: Ayush Krishnappa
"""
import math

"""
This function calculates the population of tourists given the population of bears
Returns the population of tourists
"""
def num_tourists (bears) :
    tourists = 0
    if ((bears < 4) or (bears > 15)) :
        tourists = 0
    else :
        ## uses min to meet the capacity constraint of <= 10 bears
        tourists = min((10000 * bears), (10000 * 10))
        if (bears > 10) :
            tourists += ((bears - 10) * 20000)
    return tourists

"""
This function calculates the next years values of bear population and berry field area
given the current bear population, berry field area, and tourist population. It returns
a tuple of a pair of the next years bear population and berry field area
"""
def find_next (bears, berries, tourists) :
    ## uses max to make sure bear population and berry field area is not negative
    bears_next = max(int(berries / (50 * (bears + 1)) + bears * 0.60 - (math.log(1 + tourists, 10) * 0.1)), 0)
    berries_next = max((berries * 1.5) - (bears + 1) * (berries / 14) - (math.log(1 + tourists, 10) * 0.05), 0.0)
    bear_berry = (bears_next, berries_next)
    return bear_berry


bears = input("Number of bears => ")
print(bears)
bears = int(bears)

berries = input("Size of berry area => ")
print(berries)
berries = float(berries)

## adds number of spaces needed to pad the 10 charachter column
print(('Year' + (5 * ' ')), ('Bears' + (4 * ' ')), ('Berry' + (4 * ' ')), 'Tourists' + (2 * ' '))
tourists = num_tourists(bears)
print(('1' + (8 * ' ')), (str(bears) + ((9 - len(str(bears))) * ' ')), (str(berries) + ((9 - len(str(berries))) * ' ')), str(tourists) + ((10 - len(str(tourists))) * ' '))

## lists to calculate the min and max values for each category
bearsL = []
berriesL = []
touristsL = []
i = 2
## appends first year values to the lists
bearsL.append(bears)
berriesL.append(round(berries, 1))
touristsL.append(tourists)
while (i <= 10) :
    bears, berries = find_next(bears, berries, tourists)
    tourists = num_tourists(bears)
    bearsL.append(bears)
    berriesL.append(round(berries, 1))
    touristsL.append(tourists)
    ## adds the correct number of spaces needed to pad the 10 charachter column by subtracting 
    ## the length of the string from 9
    ## subtracts from 9 since comma adds an additional space
    print((str(i) + ((9 - len(str(i))) * ' ')), (str(bears) + ((9 - len(str(bears))) * ' ')), (str(round(berries, 1)) + ((9 - len(str(round(berries, 1)))) * ' ')), str(tourists) + ((10 - len(str(tourists))) * ' '))
    i+=1

## uses min and max function for lists to calc min and max values
min_bears = str(min(bearsL))
min_berries = str(min(berriesL))
min_tourists = str(min(touristsL))
max_bears = str(max(bearsL))
max_berries = str(max(berriesL))
max_tourists = str(max(touristsL))
print()
print(('Min:' + (5 * ' ')), (min_bears + ((9 - len(min_bears)) * ' ')), (min_berries + ((9 - len(min_berries)) * ' ')), min_tourists + ((10 - len(str(min_tourists))) * ' '))
print(('Max:' + (5 * ' ')), (max_bears + ((9 - len(max_bears)) * ' ')), (max_berries + ((9 - len(max_berries)) * ' ')), max_tourists + ((10 - len(str(max_tourists))) * ' '))
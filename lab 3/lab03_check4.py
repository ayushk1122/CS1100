# -*- coding: utf-8 -*-
"""
Created on Wed Sep 29 15:04:23 2021

@author: User
"""

def calc_pop_bunnies (cur_pop_bun, cur_pop_fox) :
    cur_pop_bun = int(cur_pop_bun)
    cur_pop_fox = int(cur_pop_fox)
    next_year_pop = max(int((10 * cur_pop_bun) / (1 + 0.1 * cur_pop_bun) - 0.05 * cur_pop_bun * cur_pop_fox), 0)
    return next_year_pop

def calc_pop_fox (cur_pop_bun, cur_pop_fox) :
    cur_pop_bun = int(cur_pop_bun)
    cur_pop_fox = int(cur_pop_fox)
    next_year_pop = max(int(0.4 * cur_pop_fox + 0.02 * cur_pop_fox * cur_pop_bun), 0)
    return next_year_pop


num_bunnies = input("Number of bunnies ==> ")
num_bunnies = int(num_bunnies)
num_foxes = input("Number of foxes ==> ")
num_foxes = int(num_foxes)

year2b = calc_pop_bunnies(num_bunnies, num_foxes)
year2f = calc_pop_fox(num_bunnies, num_foxes)
year3b = calc_pop_bunnies(year2b, year2f)
year3f = calc_pop_fox(year2b, year2f)
year4b = calc_pop_bunnies(year3b, year3f)
year4f = calc_pop_fox(year3b, year3f)
year5b = calc_pop_bunnies(year4b, year4f)
year5f = calc_pop_fox(year4b, year4f)

print("Year 1: {:d} {:d}".format(num_bunnies, num_foxes))
print("Year 2: {:d} {:d}".format(year2b, year2f))
print("Year 3: {:d} {:d}".format(year3b, year3f))
print("Year 4: {:d} {:d}".format(year4b, year4f))
print("Year 5: {:d} {:d}".format(year5b, year5f))
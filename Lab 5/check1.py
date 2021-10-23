# -*- coding: utf-8 -*-
"""
Created on Tue Oct 12 21:45:13 2021

@author: Ayush Krishnappa
"""

import lab05_util

restaurants = lab05_util.read_yelp('yelp.txt')

def print_info (restaurant):
    print(restaurant[0] + ' (' + restaurant[5] + ')')
    address = restaurant[3].split('+')
    for line in address:
        if (line != '+'):
            print('\t' + line)
    total = 0
    for score in restaurant[6]:
        total += score
    average = total / (len(restaurant[6]))
    print("Average score: {:.2f}".format(average))
    print()
    
print_info(restaurants[0])
print_info(restaurants[1])
print_info(restaurants[26])
    
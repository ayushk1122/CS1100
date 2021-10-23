# -*- coding: utf-8 -*-
"""
Created on Tue Oct 12 22:14:17 2021

@author: Ayush Krishnappa
"""

import lab05_util

restaurants = lab05_util.read_yelp('yelp.txt')

id = input("Please enter an id: ").strip()
id = int(id)
    
def print_info (restaurant):
    print(restaurant[0] + ' (' + restaurant[5] + ')')
    address = restaurant[3].split('+')
    for line in address:
        if (line != '+'):
            print('\t' + line)
    total = 0
    for score in restaurant[6]:
        total += score
    if (len(restaurant[6]) > 3):
        average = (total - (max(restaurant[6]) + min(restaurant[6]))) / (len(restaurant[6]))
    else:
        average = total / (len(restaurant[6]))
        
    if (average > 0 and average <=2): 
        print("This restaurant is rated bad, based on {:d} reviews.".format(len(restaurant[6])))
    elif (average > 2 and average <= 3):
        print("This restaurant is rated average, based on {:d} reviews.".format(len(restaurant[6])))
    elif (average > 3 and average <= 4):
        print("This restaurant is rated above average, based on {:d} reviews.".format(len(restaurant[6])))
    elif (average > 4 and average <= 5):
        print("This restaurant is rated very good, based on {:d} reviews".format(len(restaurant[6])))
    print()

while(id >= 0 and id < len(restaurants)):
    print_info(restaurants[id])
    id = input("Please enter an id: ").strip()
    id = int(id)

print("Warning: That id is not valid")
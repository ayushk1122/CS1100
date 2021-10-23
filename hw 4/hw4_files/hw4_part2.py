# -*- coding: utf-8 -*-
"""
Created on Mon Oct 11 12:18:31 2021
This program determines the statistics for a user inputted week from a data set of covid cases for 
different states
This program utilizes loops, conditionals, mathematical operations, and functions to accomplish its
final product
@author: Ayush Krishnappa
"""

import hw4_util

print("...")
week = input("Please enter the index for a week: ").strip()
print(week)
week = int(week)

"""
This function takes in a week index and state abreviation and outputs the daily average
number of positive cases per week, per 100,000 for that given state and week.
"""
def daily(week, state):
    average = 0
    total = 0
    for state_list in hw4_util.part2_get_week(week):
        if (state_list[0] == state):
            i = 2
            ## while loop from index 2-8 to calculate total positive cases
            while (i <= 8):
                total += state_list[i]
                i += 1
            average = ((total / 7) / state_list[1]) * 100000
    return average

"""
This function takes in a user inputted week and state abreviation and returns the average daily
percent of positive cases for that given state and week 
"""
def pct(week, state):
    total_pos = 0
    total_neg = 0
    average_pct = 0
    for state_list in hw4_util.part2_get_week(week):
        if (state_list[0] == state):
            i = 2
            ## uses two while loops to calculate positive and negative test case totals 
            while (i <= 8):
                total_pos += state_list[i]
                i += 1
            i = 9
            while (i <= 15):
                total_neg += state_list[i]
                i += 1
            average_pct = (total_pos / (total_neg + total_pos)) * 100
    return average_pct

"""
This function takes in a user inputted week and returns a list of all the travel quarantine states
for that given week
Uses the given criteria for a travel quarantine state
"""
def quar(week):
    quar_states = []
    for state_list in hw4_util.part2_get_week(week):
        ## to avoid repeatingly asking for the state I use the first index of the looping state list
        ## to make sure I can use the daily and pct functions 
        if ((daily(week, state_list[0]) > 10) or (pct(week, state_list[0]) > 10)):
            quar_states.append(state_list[0])
    print("Quarantine states:")
    hw4_util.print_abbreviations(quar_states)
    
"""
This function takes in a user inputted week and returns the highest daily average value and the state 
it corresponds to 
"""
def high(week):
    max_avg = 0;
    max_state = ''
    for state_list in hw4_util.part2_get_week(week):
        ## same logic as quar function with using looping state list index instead of repeatedly
        ## asking for the state
        if (daily(week, state_list[0]) > max_avg):
            max_avg = daily(week, state_list[0])
            max_state = state_list[0]
    print("State with highest infection rate is", max_state)
    print("Rate is {:.1f} per 100,000 people".format(max_avg))
    
"""
While loop to run the simulation
Uses all above functions in loop and prints in loop to avoid any repeated print statements 
"""
while (week > 0):
    ## makes sure the week index is a valid index
    if (week < (len(hw4_util.part2_get_week(week)) - 1)):
        request = input("Request (daily, pct, quar, high): ").strip()
        print(request)
        ## to avoid case sensitivity 
        request = request.lower()
        if (request == 'daily'):
            state = input("Enter the state: ").strip()
            print(state)
            ## this is used to check if a state is not within the list
            ## by checking to 0, it does not overlap with the actual value for daily() being 0 since
            ## value would acutally be 0.0 not 0
            ## therefore only possible way for daily(week, state) being the int 0 would be if
            ## the state is not within the list
            if (daily(week, state) == 0):
                print("State", state, "not found")
            else:
                print("Average daily positives per 100K population: {:.1f}".format(daily(week, state)))
        elif (request == 'pct'):
            state = input("Enter the state: ").strip()
            print(state)
            ## same logic as conditional above
            if (pct(week, state) == 0):
                print("State", state, "not found")
            else:
                print("Average daily positive percent: {:.1f}".format(pct(week, state)))
        elif (request == 'quar'):
            quar(week)
        elif (request == 'high'):
            high(week)
        else:
            ## if the request is not valid it prints this 
            print("Unrecognized request")
        print("...")
    else:
        print("No data for that week")
        print("...")
    week = input("Please enter the index for a week: ").strip()
    print(week)
    week = int(week)
        
        
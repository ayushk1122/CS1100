# -*- coding: utf-8 -*-
"""
Created on Mon Sep 13 12:57:28 2021
This program takes values of minutes, seconds, miles, and target miles to computer pace, 
speed, and the time it takes to travel the number of target miles at the respective pace. 
Professor Turner - CS 1100
@author: Ayush Krishnappa
"""

minutes = input("Minutes ==> ")
print(minutes)

seconds = input("Seconds ==> ")
print(seconds)

miles = input("Miles ==> ")
print(miles)

target_miles = input("Target Miles ==> ")
print(target_miles)

minutes = int(minutes)
seconds = int(seconds)
miles = float(miles)
target_miles = float(target_miles)

pace_calc = (minutes * 60 + seconds)
pace_calc_sec = pace_calc / miles
pace_sec = int(pace_calc_sec % 60)
pace_min = int((pace_calc_sec / 60))

speed = miles / ((minutes + (seconds / 60)) / 60)

run_calc = pace_calc_sec * target_miles
run_time_min = int(run_calc / 60)
run_time_sec = int(run_calc % 60)


print()
print("Pace is", pace_min, "minutes and", pace_sec, "seconds per mile.")
print("Speed is {:.2f} miles per hour.".format(speed))
print("Time to run the target distance of {:.2f} miles is {:.0f} minutes and {:.0f} seconds.".format(target_miles, run_time_min, run_time_sec))

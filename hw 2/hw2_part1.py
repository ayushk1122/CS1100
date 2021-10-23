# -*- coding: utf-8 -*-
"""
Created on Thu Sep 16 14:27:33 2021

@author: User
"""
import math

def find_volume_sphere(radius):
    volume = float(4/3) * math.pi * (float(radius)**3)
    return volume

def find_volume_cube(side):
    volume = float(side)**3
    return volume

user_radius = input("Enter the gum ball radius (in.) => ")
print(user_radius)

weekly_sales = input("Enter the weekly sales => ")
print(weekly_sales)
print()

user_radius = float(user_radius)
weekly_sales = float(weekly_sales)
target_sales = 1.25 * weekly_sales
diameter = user_radius * 2
##number of gumballs machine must hold on each edge to meet weekly sales, correct
cube_side_gumballs = math.ceil(math.pow(target_sales, 1/3))  

##correct
edge_size_in = cube_side_gumballs * diameter

volume_of_cube = find_volume_cube(edge_size_in)

volume_of_gum_ball = find_volume_sphere(user_radius)


total_number_gum_balls = math.pow(cube_side_gumballs, 3)
extra_gumballs = total_number_gum_balls - target_sales

wasted_space_target = volume_of_cube - (volume_of_gum_ball * math.ceil(target_sales))

wasted_space_filled = volume_of_cube - (volume_of_gum_ball * total_number_gum_balls)

print("The machine needs to hold", cube_side_gumballs, "gum balls along each edge.")
print("Total edge length is {:.2f} inches.".format(edge_size_in))
print("Target sales were", str(math.ceil(target_sales)) + ", but the machine will hold", int(extra_gumballs), "extra gum balls.")
print("Wasted space is {:.2f} cubic inches with the target number of gum balls,".format(wasted_space_target))
print("or {:.2f} cubic inches if you fill up the machine.".format(wasted_space_filled))








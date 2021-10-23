# -*- coding: utf-8 -*-
"""
Created on Mon Oct  4 12:59:12 2021
This program runs a simulation for a user inputted number of turns and the given name for
a Pikachu while also creating encounters with wild pokemon for an inputted often number of times.
This program uses tuples, lists, and loops to accomplish its objective. 
@author: Ayush Krishnappa
"""
turns = input("How many turns? => ")
print(turns)
turns = int(turns)

name = input("What is the name of your pikachu? => ")
print(name)

often = input("How often do we see a Pokemon (turns)? => ")
print(often)
often = int(often)

##global variable new direction to update for different moves
new_direction = ''

"""
This function returns the new coordinates for the pokemon given the original coordinates, a 
direction, and the number of steps taken
The function returns a tuple of the x and y coordinates of the pokemon
"""
def move_pokemon (coor, direction, steps):
    direction = direction.lower()
    row = coor[0]
    column = coor[1]
    ## conditonal block to calc new coordinates given a direction
    ## uses max to make sure coordinates don't go out of boundary
    if (direction == 'n') :
        row = max((row - steps), 0)
    elif(direction == 'e') :
        column = min((column + steps), 150)
    elif(direction == 's') :
        row = min((row + steps), 150)
    elif(direction == 'w') :
        column = max((column - steps), 0)
    else :
        row = row 
        column = column 
    ncoor = (row , column)
    return ncoor

"""
This function simulates the pokemon encounter with a wild pokemon that takes place every so often
turns. It calculates the new coordinates given the type of pokemon encountered, and also updates
the record list of wins and losses. The function returns the new coordinates of the pokemon given 
the current coordinates, the current record list, and the current direction. 
"""
def pokemon_encounter (coor, record, direction) :
    print("Turn", str(i) + ",", name, "at", coor)
    ptype = input("What type of pokemon do you meet (W)ater, (G)round? => ")
    print(ptype)
    ptype = ptype.lower()
    direction = direction.lower()
    ## conditional block for the type of pokemon g = ground, w = water
    ## calls move_pokemon to update the coordinates for the corresponding encounter
    if (ptype == 'g') :
        if (direction == 'n') :
            new_direction = 's'
        elif (direction == 'e') :
            new_direction = 'w'
        elif (direction == 's'):
            new_direction = 'n'
        elif (direction == 'w') :
            new_direction = 'e'
        else :
            new_direction = direction
        ncoor = move_pokemon(coor, new_direction, 10)
        print(name, 'runs away to', ncoor)
        record.append('Lose')
    elif (ptype == 'w') :
        if (direction == 'n') :
            new_direction = 'n'
        elif (direction == 'e') :
            new_direction = 'e'
        elif (direction == 's') :
            new_direction = 's'
        elif (direction == 'w') :
            new_direction = 'w'
        else :
            new_direction = direction
        ncoor = move_pokemon(coor, new_direction, 1)
        print(name, "wins and moves to", ncoor)
        record.append("Win")
    else :
        new_direction = direction
        ncoor = move_pokemon(coor, new_direction, 0)
        record.append("No Pokemon")
    return ncoor

i = 1
coor = (75, 75)
record = []

print()
print("Starting simulation, turn 0", name, "at", coor)
while (i <= turns) :
    direction = input("What direction does " + name + " walk? => ")
    print(direction)
    ## calculates initial coordinates 
    coor = move_pokemon(coor, direction, 5)
    ## uses % to calulate when to trigger pokemon encounter
    if ((i % often) == 0) :
        coor = pokemon_encounter(coor, record, direction)
    i += 1
    
print(name, "ends up at", str(coor) + ",", "Record:", str(record))
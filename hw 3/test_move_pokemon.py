# -*- coding: utf-8 -*-
"""
Created on Mon Oct  4 13:24:29 2021

@author: User
"""

from hw3_part2 import move_pokemon
row = 15
column = 10
print ( move_pokemon ( ( row , column ) , 'n' , 20 ) ) # s h o ul d p r i n t ( 0 , 10)
print ( move_pokemon ( ( row , column ) , 'e' , 20 ) ) # s h o ul d p r i n t ( 1 5 , 30)
print ( move_pokemon ( ( row , column ) , 's' , 20 ) ) # s h o ul d p r i n t ( 3 5 , 10)
print ( move_pokemon ( ( row , column ) , 'w' , 20 ) ) # s h o ul d p r i n t ( 1 5 , 0)
row = 135
column = 140
print ( move_pokemon ( ( row , column ) , 'N' , 20 ) ) # s h o ul d p r i n t ( 1 1 5 , 140)
print ( move_pokemon ( ( row , column ) , 'E ' , 20 ) ) # s h o ul d p r i n t ( 1 3 5 , 150)
print ( move_pokemon ( ( row , column ) , 'S ' , 20 ) ) # s h o ul d p r i n t ( 1 5 0 , 140)
print ( move_pokemon ( ( row , column ) , 'W' , 20 ) ) # s h o ul d p r i n t ( 1 3 5 , 120)

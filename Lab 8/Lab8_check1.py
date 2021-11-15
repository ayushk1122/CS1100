# -*- coding: utf-8 -*-
"""
Created on Tue Nov  2 14:33:05 2021

@author: Ayush
"""

def get_words (descrip):
    output = set()
    dsplit = descrip.split()
    for i in range(len(dsplit)):
        dsplit[i] = dsplit[i].replace('.', '')
        dsplit[i] = dsplit[i].replace(',', '')
        dsplit[i] = dsplit[i].replace('(', '')
        dsplit[i] = dsplit[i].replace(')', '')
        dsplit[i] = dsplit[i].replace('\"', '')
        
        dsplit[i] = dsplit[i].lower()
        
        if (dsplit[i].isalpha() and len(dsplit[i]) >= 4):
            output.add(dsplit[i])
    
    return output

file1 = open('wrpi.txt')
club = file1.readline()
clubs = club.split('|')
print(get_words(clubs[1]))
            
print()

file2 = open('csa.txt')
club = file2.readline()
clubs = club.split('|')
print(get_words(clubs[1]))        
        
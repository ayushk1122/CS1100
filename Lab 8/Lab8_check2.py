# -*- coding: utf-8 -*-
"""
Created on Tue Nov  2 14:48:40 2021

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
club1 = file1.readline()
clubs1 = club1.split('|')

            
file2 = open('csa.txt')
club2 = file2.readline()
clubs2 = club2.split('|')

club1words = get_words(clubs1[1])
club2words = get_words(clubs2[1])

print('Comparing clubs ' + clubs1[0] + ' and ' + clubs2[0] + ':')
print('Same words: {}'.format(club1words.intersection(club2words)))
print()
print('Unique to {}: {}'.format(clubs1[0], club1words.union(club2words)))
print()
print('Unique to {}: {}'.format(clubs2[0], club2words.union(club1words)))

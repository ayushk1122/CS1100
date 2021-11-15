# -*- coding: utf-8 -*-
"""
Created on Wed Nov  3 13:56:49 2021

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

file1 = open('csa.txt')
club1 = file1.readline()
clubs1 = club1.split('|')
club1_words = get_words(clubs1[1])

            
file2 = open('allclubs.txt')

club1words = get_words(clubs1[1])
output = [() for i in range(1)]

for line in file2:
    club2 = line.split('|')
    if (club2[0] != clubs1[0]):
        club_d = club2[1]
        club_d_word = get_words(club_d)
        similarity = len(club1_words.intersection(club_d_word))
        output.append((similarity, club2[0]))
    
    
    
output.sort()
print(output[-1], output[-2], output[-3], output[-4], output[-5])


# -*- coding: utf-8 -*-
"""
Created on Mon Nov  8 15:51:00 2021

@author: Ayush
"""

dfile = input("Dictionary file => ")
print(dfile)
ifile = input("Input file => ")
print(ifile)
kfile = input("Keyboard file => ")
print(kfile)


def found (word, dictionary):
    if (word in dictionary.keys()):
        return True
    
def drop (word, dictionary):
    candidates = set()
    for letter in word:
        temp_word = word
        drop_word = temp_word.replace(letter, '')
        if (drop_word in dictionary.keys()):
            candidates.add(drop_word)
    return candidates

def insert (word, dictionary, candidates):
    for letter in word:
        for i in range (len(word)):
            candidate = word[0:i:] + letter + word[i::]
            if (candidate in dictionary.keys()):
                candidates.add(candidate)
    return candidates

def swap (word, dictionary, candidates):
    
    
        
    



















## main body of program
if __name__ == '__main__':
    ## moves contents of dictionary file into a python dictionary 
    edict = dict()
    
    for line in open(dfile):
        split = line.split(',')
        edict[split[0]] = float(split[1].strip())
        
    ## moves contents of keyboard file into a python dictionary 
    ## first letter as key rest of adjacent letters as value in list form
    kdict = dict()
    
    for line in open(kfile):
        split = line.split()
        key = split[0]
        split.remove(key)
        values = split
        kdict[key] = values
        
    
    ## executive program
    """
    for word in open(ifile):
        if (found(word, edict)):
            print(word)
        else:
            drop(word)
            insert(word)
            swap(word)
            replace(word)
    """
    
        
    
    

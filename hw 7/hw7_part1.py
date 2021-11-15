# -*- coding: utf-8 -*-
"""
Created on Mon Nov  8 15:51:00 2021
This program takes an 3 inputted files: a dictionary file, an input file, and a keyboard file
It then autocorrects each word in the input file using the given criteria in the spec
Then it prints statistics about how many of the autocorrected words were found
in a dictionary of english words
@author: Ayush
"""

dfile = input("Dictionary file => ")
print(dfile)
ifile = input("Input file => ")
print(ifile)
kfile = input("Keyboard file => ")
print(kfile)

"""
This function takes a string word and a dictionary as input and returns true
if the word is in the dictionary 
"""
def found (word, dictionary):
    if (word in dictionary.keys()):
        return True

"""
This function takes a string word, dictionary, and a set of candidates as input
and returns an updated set of candidates with different autocorrected words using the drop method
"""
def drop (word, dictionary, candidates):
    ## word list used to avoid removing duplicate letters
    word_list = list(word)
    
    for i in range(len(word_list)):
        ## temporary list used to make sure original word list is not changed
        ## hence uses copy as well to avoid aliasing 
        temp_list = word_list.copy() 
        temp_list.pop(i) ## removes value at certain index
        drop_word = ''.join(temp_list)
        if (drop_word in dictionary.keys()):
            candidates.add(drop_word)
    return candidates

"""
This function takes a string word, dictionary, and set of candidates as input
and returns an updated set of candidates with autocorrected words using the input method
"""
def insert (word, dictionary, candidates):
    ## list of all letters to use for insert
    alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r'
                ,'s','t','u','v','w','x','y','z']
    
    for index in range(len(word) + 1):
        for i in range (len(alphabet)):
            ## inserts each letter from alphabet list into the word using slicing
            candidate = word[0:index:] + alphabet[i] + word[index::]
            if (candidate in dictionary.keys()):
                candidates.add(candidate)
        index += 1
    return candidates

"""
This function takes a string word, dictionary, and set of candidates as input
and returns an updated set of candidates with autocorrected words using the swap method
"""
def swap (word, dictionary, candidates):
    ## word list used for easier indexing 
    word_list = list(word)
    for i in range(len(word_list) - 1):
        ## temp list and copy to avoid aliasing and changing original list
        temp_list = word_list.copy() 
        temp = temp_list[i] ## temp variable to store index
        temp_list[i] = temp_list[i+1]
        temp_list[i+1] = temp
        word = ''.join(temp_list) ## uses join to convert list back into string 
        if (word in dictionary.keys()):
            candidates.add(word)
    return candidates

"""
This function takes a string word, dictionary, set of candidates, and a keyboard dictionary 
and returns an updated set of candidates with autocorrected words using the replace method
"""
def replace (word, dictionary, candidates, keyboard):
    word_list = list(word)
    for i in range(len(word_list)):
        if (word_list[i] in keyboard.keys()):
            ## loops through each letter in the list value of the keyboard dictionary
            for value in keyboard[word_list[i]]:
                ## uses copy to avoid aliasing 
                temp_list = word_list.copy()
                temp_list[i] = value
                temp_word = ''.join(temp_list) ## converts list back into string
                if (temp_word in dictionary.keys()):
                    candidates.add(temp_word)     
    return candidates

"""
This function takes a set of candidates and a dictionary and returns a sorted list
of tuples with each value being a (frequency, word) tuple
"""
def sort_candidates (candidates, dictionary):
    output = []
    for candidate in candidates:
        output.append((dictionary[candidate], candidate))
    
    ## sorts list from greatest to least by frequency 
    output.sort(reverse = True)
    ## checks for cases of exact same frequency for different words 
    for i in range (len(output) - 1):
        if (output[i][0] == output[i+1][0]):
            ## if frequency is the same and first word is earlier lexographically then
            ## the next word, swaps them
            if (output[i][1] < output[i+1][1]):
                temp = output[i]
                output[i] = output[i+1]
                output[i+1] = temp
    return output
    


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
        
    
    ## statistics formatted
    for word in open(ifile):
        word = word.strip()
        output = ''
        spaces = 15 - len(word)
        if (found(word, edict)):
            output += (' ' * spaces) + word + ' -> ' + 'FOUND'
            print(output)
        else:
            ## passes updated candidates set to each concurrent method and adds on to it
            ## instead of making a new set each time
            candidates = set()
            candidates1 = drop(word, edict, candidates)
            candidates2 = insert(word, edict, candidates1)
            candidates3 = swap(word, edict, candidates2)
            candidates4 = replace(word, edict, candidates3, kdict)
    
            ## sorted list of tuples
            sorted_candidates = sort_candidates(candidates4, edict)
            
            ## formats spacing using conditionals based off length of list of tuples
            ## conditional block to determine what to print next to word
            if (len(sorted_candidates) == 0):
                output += (' ' * spaces) + word + ' -> ' + 'NOT FOUND'
                print(output, end = '\n')
            elif (len(sorted_candidates) <= 3):
                output += (' ' * spaces) + word + ' -> ' + 'FOUND' + '  ' + str(len(sorted_candidates)) + ':  '
                for candidate in sorted_candidates:
                    if (candidate != sorted_candidates[len(sorted_candidates) - 1]):
                        output += candidate[1] + ' '
                    else:
                        output += candidate[1]
                print(output, end = '\n')
            else:
                if (len(sorted_candidates) >= 10):
                    output += (' ' * spaces) + word + ' -> ' + 'FOUND' + ' ' + str(len(sorted_candidates)) + ':  '
                else:
                    output += (' ' * spaces) + word + ' -> ' + 'FOUND' + '  ' + str(len(sorted_candidates)) + ':  '
                for i in range (3):
                    if (i != 2):
                        output += sorted_candidates[i][1] + ' '
                    else:
                        output += sorted_candidates[i][1]
                print(output, end = '\n')

        
    
    

# -*- coding: utf-8 -*-
"""
Created on Sun Oct 31 14:14:39 2021
This program takes two files and outputs different statistics of these two files
This program uses lists, sets, loops, string methods, and function organization
to accomplish its goal
@author: Ayush Krishnappa
RIN: 662028478
"""

stop_words = 'stop.txt'
doc1 = input ('Enter the first file to analyze and compare ==> ')
print(doc1)
doc2 = input ('Enter the second file to analyze and compare ==> ')
print(doc2)
max_sep = input ('Enter the maximum separation between words in a pair ==> ')
print(max_sep)
max_sep = int(max_sep)
print()
    
"""
This function removes the spaces from a each string in a line of text and 
surrounding white space characters
Takes a list of strings as input and returns a trimmed list of strings as output
"""
def remove_spaces (l1):
    i = 0
    while (i < len(l1)):
        if (l1[i] == ''):
            l1.remove(l1[i]) 
            i-=1
        else:
            l1[i] = l1[i].strip()
            i+=1
    return l1

"""
This function removes non alphabetical characters from a list of strings
removes spaces and converts each string to lower case.
Takes a list of strings as output and returns edited list of strings
"""
def remove_non_letter (l1):
    i = 0
    while (i < len(l1)):
        for s in l1[i]:
            if(s.isalpha() == False):
                l1[i] = l1[i].replace(s, '')
        
        if (l1[i] == ''):
            l1.remove(l1[i])
            i-=1
        else:
            l1[i].lower()
            i+=1
            
    return l1

"""
This function removes any words in the list that are also in the set of 
stop words
Function takes a list of strings and a set of stop words as input
Returns edited list of strings
"""
def remove_stop_words (l1, stop_ws):
    i = 0
    while (i < len(l1)):
        l1[i] = l1[i].lower()
        if (l1[i] in stop_ws):
            l1.remove(l1[i])
            i -= 1
        else:
            i += 1
    return l1

"""
This function calculates the average word length of each word in a list
of strings
Takes a list of strings as input
Returns a float average
"""
def avg_word_len (l1):
    average = 0.0
    for word in l1:
        average += (len(word))
    
    average = round(average / len(l1), 2)
    return average 
    
"""
This function takes a list of strings and finds the number of words for 
a certain word length from [1 - max word length] and adds the words of the
respectable size to a list
Takes a list of strings as input
Returns list of words with each index corresonding to a word length
"""
def find_word_len (l1):
    length = 1
    word_len_index = 0
    max_len = find_max_len(l1)
    ## list of lists, each list holds the words of a certian word length
    ## with each index representing the word length starting from index 0 = word len 1
    word_len = [[] for i in range(max_len)]
    
    while (length < (max_len + 1)):
        for i in range(len(l1)):
            if (len(l1[i]) == length and (word_len[word_len_index].count(l1[i]) == 0)):
                word_len[word_len_index].append(l1[i])
        word_len[word_len_index].sort()
        word_len_index += 1
        i+=1
        length+=1
    return word_len

"""
This function prints the word lengths in the correct format 
Takes list of strings and word length list as input 
Returns string output of formatting 
"""
def print_word_len (l1, word_len):
    output = ''
        
    length = 1
    for i in range (len(word_len)):
        if (len(word_len[i]) == 0 and length < 10):
            output += ((' ' * 3) + str(length) + ':' + (3 * ' ') + '0:' + '\n')
        elif (len(word_len[i]) == 0 and length >= 10):
            output += ((' ' * 2) + str(length) + ':' + (3 * ' ') + '0:' + '\n')
        else:
            if (len(word_len[i]) < 10 and length < 10):
                output += ((' ' * 3) + str(length) + ':' + (3 * ' ') + str(len(word_len[i])) + ': ')
            elif (length >= 10 and len(word_len[i]) < 10):
                output += ((' ' * 2) + str(length) + ':' + (3 * ' ') + str(len(word_len[i])) + ': ')
            elif (length < 10 and len(word_len[i]) >= 10):
                output += ((' ' * 3) + str(length) + ':' + (2 * ' ') + str(len(word_len[i])) + ': ')
            else:
                output += ((' ' * 2) + str(length) + ':' + (2 * ' ') + str(len(word_len[i])) + ': ')
            if (len(word_len[i]) <= 6):
                for j in range(len(word_len[i])):
                    if (word_len[i][j] != word_len[i][len(word_len[i]) - 1]):
                        output += (word_len[i][j] + ' ')
                    else:
                        output += (word_len[i][j])
                if (i != len(word_len) - 1):
                    output += '\n'
            else:
                word_len[i].sort()
                output += (word_len[i][0] + ' ' + word_len[i][1] + ' ' + word_len[i][2])
                output += ' ... '
                output += (word_len[i][len(word_len[i]) - 3] + ' ' + word_len[i][len(word_len[i]) - 2] + ' ' + word_len[i][len(word_len[i]) - 1])
                if (i != len(word_len) - 1):
                    output += '\n'
        length += 1
            
    return output

"""
This function takes a list of strings and finds the longest stringin the list
Takes list of strings as input 
Returns int value for longest string length
"""
def find_max_len (l1):
    max_len = 0
    for words in l1:
        if (len(words) > max_len):
            max_len = len(words)
                
    return max_len

"""
This function takes a list of strings and a user inputted max seperator value
and finds the word pairs for the list of strings
Takes list of strings and max sep as input
Returns list of lists containing the word pairs 
"""
def find_word_pairs (l1, max_sep):
    ## list of lists used to hold each word pair in a list
    word_pairs = [() for i in range (1)]
    for i in range (len(l1)):
        j = i + 1
        while (j < (len(l1))):
            ## makes sure second string of word pair is not too distant from
            ## first string of word pair
            if ((j - i) > max_sep):
                break
            ## Don't sort word pairs here since it may create duplicates wil sort seperatly 
            else:
                word_pairs.append((l1[i], l1[j]))
            j+=1
    
    word_pairs.remove(())
        
    return word_pairs

"""
This function takes a list of strings, user inputted max seperator value, and
word pairs list as input and finds the distinct pairs 
Returns distinct pairs set
"""
def find_dist_pairs (l1, max_sep, word_pairs):
    ## sorts word pairs alphabetically 
    word_pairs = sort_word_pairs(word_pairs)
        
    dist_pairs = set(() for i in range (1))
    for pair in word_pairs:
        ## checks to make sure word pair is distinct according to definition given
        if ((pair[1], pair[0]) not in word_pairs or (pair[0] == pair[1])):
            dist_pairs.add((pair[0], pair[1]))
            
    dist_pairs.remove(())
        
    return dist_pairs
      
"""
This function takes the set of dist_pairs and list of word pairs as input and returns
the ratio between their lengths 
"""
def calc_dist_ratio (dist_pairs, word_pairs):
    return (len(dist_pairs) / len(word_pairs))

"""
This function takes the list of word pairs and set of distinct pairs and 
returns a string output variable of the correct formatting of the word pairs 
"""
def format_word_pairs (word_pairs, dist_pairs):
    i = 0
    word_pairs = sort_word_pairs(word_pairs)
    word_pairs_output = ''
    
    ## checks to make sure which formatting to use based of number of distinct pairs
    if (len(dist_pairs) > 5):
        for i in range (5):
            word_pairs_output += ('  ' + word_pairs[i][0] + ' ' + word_pairs[i][1] + '\n')
        word_pairs_output += ('  ...' + '\n')
        i = -5
        while (i <= -1):
            if (i != -1):
                word_pairs_output += ('  ' + word_pairs[i][0] + ' ' + word_pairs[i][1] + '\n')
            else:
                word_pairs_output += ('  ' + word_pairs[i][0] + ' ' + word_pairs[i][1])
            i += 1
    else:
        for i in range (5):
            if (i != 4):
                word_pairs_output += ('  ' + word_pairs[i][0] + ' ' + word_pairs[i][1] + '\n')
            else:
                word_pairs_output += ('  ' + word_pairs[i][0] + ' ' + word_pairs[i][1])
                
    return word_pairs_output

"""
This function prints the correct formatting of the different word lengths and their 
counts, as well as the corresponding words for each count for the jaccard calculations
Takes both word length lists as input
Prints correct formatting no return 
"""
def print_jac_word_len (word_len1, word_len2):
    ## converts each list within the list to a set to remove duplicates 
    for i in range (len(word_len1)):
        word_len1[i] = set(word_len1[i])
    for i in range (len(word_len2)):
        word_len2[i] = set(word_len2[i])
    
    length = 1
    ## calculates the jaccard calculation for each word length index between the 
    ## two word length lists 
    ## Loops through the min of the two lengths to avoid index out of bounds
    for i in range (min(len(word_len1), len(word_len2))):
        if (len(word_len1[i].union(word_len2[i])) != 0):
            jac_sim = len(word_len1[i].intersection(word_len2[i])) / len(word_len1[i].union(word_len2[i]))
        else:
            jac_sim = 0.0
        if (length < 10):
                print('   {:d}: {:.4f}'.format(length, jac_sim), end = '\n')
        elif (length >= 10):
                print('  {:d}: {:.4f}'.format(length, jac_sim), end = '\n')
        length += 1
    
    ## loops through the remaining values from the minimum of the two lists lengths
    ## to the maximum of the two list lengths
    ## Prints 0 for all the calculations since the smaller word len list will not
    ## have values for these indexes
    difference = max(len(word_len1), len(word_len2)) - min(len(word_len1), len(word_len2))
    for i in range (difference):
        if ((i + (min(len(word_len1), len(word_len2))) + 1) >= 10):
            print('  {:d}: 0.0000'.format((i + (min(len(word_len1), len(word_len2)) + 1))), end = '\n')
        else:
            print('   {:d}: 0.0000'.format((i + (min(len(word_len1), len(word_len2)) + 1))), end = '\n')
           
"""
This is a seperate sorting funciton to sort a given list of word pairs
Decided to do this instead of sorting in word pairs funciton to avoid errors 
Takes word pairs list as input and returns a sorted word pairs list
"""
def sort_word_pairs (word_pairs):
    i = 0
    ## converts word pairs to a sorted list
    word_pairs = sorted(word_pairs)
    ## sorts each individual word pair and converts to a list
    while (i < len(word_pairs)):
        word_pairs[i] = sorted(word_pairs[i])
        i+=1
        
    i = 0
    ## removes any duplicates from the list of lists
    ## manually removes duplicates as want to keep it as a list
    while (i < len(word_pairs)):
        check = [word_pairs[i][0], word_pairs[i][1]]
        if (word_pairs.count(check) > 1):
            word_pairs.remove(check)
            i -= 1
        i+=1
                
    ## converts each individual word pair back to a tuple to avoid unhashable error of 
    ## lists 
    word_pairs = sorted(word_pairs)
    for i in range (len(word_pairs)):
        word_pairs[i] = (word_pairs[i][0], word_pairs[i][1])
        
    return word_pairs
    
"""
This function is made to avoid repittion of printing the output in the main body
Takes all the necesary values as input to print the correct output, essentially 
all variables created in main
"""
def print_output (doc, f_list, f_set, word_len, word_pairs, dist_pairs):
    print("Evaluating document " + doc)
    print('1. Average word length: {:.2f}'.format(avg_word_len(f_list)))
    print('2. Ratio of distinct words to total words: {:.3f}'.format(len(f_set) / len(f_list)))
    print('3. Word sets for document ' + doc + ':')
    word_len = find_word_len(f_list)
    print(print_word_len(f_list, word_len))
    print('4. Word pairs for document ' + doc)
    word_pairs = find_word_pairs(f_list, max_sep)
    dist_pairs = find_dist_pairs(f_list, max_sep, word_pairs)
    print('  ' + str(len(dist_pairs)) + ' distinct pairs')
    print(format_word_pairs(word_pairs, dist_pairs))
    print('5. Ratio of distinct word pairs to total: {:.3f}'.format(calc_dist_ratio(dist_pairs, word_pairs)))
    print()
    
## main body of program
if __name__ == '__main__':
    ## encoding to remove any accented characters 
    f1 = open(doc1, encoding = "UTF-8")
    f2 = open(doc2, encoding = "UTF-8")
    stop_words_f = open(stop_words)
    
    ## splits each file into a list of strings 
    f1_list = f1.read().strip().split()
    f2_list = f2.read().strip().split()
    stop_words_f_list = stop_words_f.read().strip().split()
    
    ## removes spaces and new line and tab characters from each string in list
    f1_list = remove_spaces(f1_list)
    f2_list = remove_spaces(f2_list)
    stop_words_f_list = remove_spaces(stop_words_f_list)
    
    ## removes all non letters from each string of list
    f1_list = remove_non_letter(f1_list)
    f2_list = remove_non_letter(f2_list)
    stop_words_f_list = remove_non_letter(stop_words_f_list)
    ## converts list of stop words to a set of stop words
    stop_words_f_set = set(stop_words_f_list)
    
    ## removes any strings that are in the stop words file from each list
    f1_list = remove_stop_words(f1_list, stop_words_f_set)
    f2_list = remove_stop_words(f2_list, stop_words_f_set)
    
    ## uses set to removes duplicates from each list 
    f1_set = set(f1_list)
    f2_set = set(f2_list)

    ## file 1   
    word_len1 = find_word_len(f1_list)
    word_pairs1 = find_word_pairs(f1_list, max_sep)
    dist_pairs1 = find_dist_pairs(f1_list, max_sep, word_pairs1)
    print_output(doc1, f1_list, f1_set, word_len1, word_pairs1, dist_pairs1)


    ## file 2
    word_len2 = find_word_len(f2_list)
    word_pairs2 = find_word_pairs(f2_list, max_sep)
    dist_pairs2 = find_dist_pairs(f2_list, max_sep, word_pairs2)
    print_output(doc2, f2_list, f2_set, word_len2, word_pairs2, dist_pairs2)
    
    ## summary comparison statistics 
    print('Summary comparison')
    if (avg_word_len(f1_list) > avg_word_len(f2_list)):
        print('1. ' + doc1 + ' on average uses longer words than ' + doc2)
    elif (avg_word_len(f1_list) < avg_word_len(f2_list)):
        print('1. ' + doc2 + ' on average uses longer words than ' + doc1)

    ## jaccard calculation for word use between the 2 files 
    jaccard_word_use = len(f1_set.intersection(f2_set)) / len(f1_set.union(f2_set))
    print('2. Overall word use similarity: {:.3f}'.format((jaccard_word_use)))
    
    print('3. Word use similarity by length:')
    print_jac_word_len(word_len1, word_len2)
    
    ## sorts each word pair to make sure the intersection is not incorrectly determined 
    sorted_word_pair1 = sort_word_pairs(word_pairs1)
    sorted_word_pair2 = sort_word_pairs(word_pairs2)
    word_pairs1_set = set(sorted_word_pair1)
    word_pairs2_set = set(sorted_word_pair2)
    
    ## jaccard calculation for both word pairs
    jac_word_pair = len(word_pairs1_set.intersection(word_pairs2_set)) / (len(word_pairs1_set.union(word_pairs2_set)))
    print('4. Word pair similarity: {:.4f}'.format(jac_word_pair))




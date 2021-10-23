# -*- coding: utf-8 -*-
"""
Created on Mon Oct  4 10:00:23 2021
This program calculates various statistics for a paragraph inputted by the user. The program
utilizes lists and loops to calculate these statistics.
@author: Ayush Krishnappa
"""

import syllables

paragraph = input("Enter a paragraph => ")
print(paragraph)

"""
calculates average sentence length
"""
sentences = paragraph.split(".")
## subtracts 1 from the len since sentence ends in a period
num_sentences = len(sentences) - 1
words = paragraph.split()
num_words = len(words)
average_sentence_len = num_words / num_sentences

"""
calculates percent hard words
"""
## new list to hold the new words for the hard word
phw = []
i = 0
## count variable to keep count of the number of hard words
count = 0;
while (i < len(words)) :
    ## checks if word is over 3 syllables
    if ((syllables.find_num_syllables(words[i]) >= 3)) :
        ## makes sure word does not have a hyphin in it and does not ends with ed or es
        if ((words[i].count("-") == 0) and ((words[i].endswith("ed") == False) or (words[i].endswith("es") == False))):
            ## incriments count variable
            count += 1
            ## adds word to new list
            if (phw.count(words[i]) == 0):
                phw.append(words[i])
    i += 1

## calculates percentage value of hard words
phw_calc = (count / len(words)) * 100.0

"""
calculates average number of syllables
"""
total_syllables = 0
i = 0
while (i < len(words)) :
    ## calculates total number of syllables in paragraph
    total_syllables += syllables.find_num_syllables(words[i])
    i += 1
asyl = total_syllables / len(words)

"""
calculates GFRI using formula given
"""
gfri = 0.4 * (average_sentence_len + phw_calc)

"""
calculates fkri using formula given
"""
fkri = 206.835 - 1.015 * average_sentence_len - 86.4 * asyl

print("Here are the hard words in this paragraph:")
print(phw)
print("Statistics: ASL:{:.2f} PHW:{:.2f}% ASYL:{:.2f}".format(average_sentence_len, phw_calc, asyl))
print("Readability index (GFRI): {:.2f}".format(gfri))
print("Readability index (FKRI): {:.2f}".format(fkri))


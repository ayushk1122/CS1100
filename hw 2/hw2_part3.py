# -*- coding: utf-8 -*-
"""
Created on Sun Sep 19 11:19:37 2021

@author: User
"""

sentence = input("Enter a sentence => ")
print(sentence)

def number_happy(u_sentence):
    return u_sentence.count('laugh') + u_sentence.count('happiness') + u_sentence.count('love') + u_sentence.count('excellent') + u_sentence.count('good') + u_sentence.count('smile')
            
def number_sad(u_sentence):
    return u_sentence.count('bad') + u_sentence.count('sad') + u_sentence.count('terrible') + u_sentence.count('horrible') + u_sentence.count('problem') + u_sentence.count('hate')
            
sentence = sentence.lower()

happy_num = number_happy(sentence)
sad_num = number_sad(sentence)

print("Sentiment:", ('+' * happy_num) + ('-' * sad_num))

if(happy_num > sad_num) :
    print("This is a happy sentence.")
elif(sad_num > happy_num) :
    print("This is a sad sentence.")
else :
    print("This is a neutral sentence.")

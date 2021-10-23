# -*- coding: utf-8 -*-
"""
Created on Sat Sep 18 13:53:43 2021

@author: User
"""

sentence = input("Enter a string to encode ==> ")
print(sentence)

def encrypt(word):
    word = word.replace(' a', '%4%')
    word = word.replace('he', '7!')
    word = word = word.replace('e', '9(*9(')
    word = word.replace('y', '*%$')
    word = word.replace('u', '@@@')
    word = word.replace('an', '-?')
    word = word.replace('th', '!@+3')
    word = word.replace('o', '7654')
    word = word.replace('9', '2')
    word = word.replace('ck', '%4')
    return word
    
def decrypt(word):
    word = word.replace('%4', 'ck')
    word = word.replace('2', '9')
    word = word.replace('7654', 'o')
    word = word.replace('!@+3', 'th')
    word = word.replace('-?', 'an')
    word = word.replace('@@@', 'u')
    word = word.replace('*%$', 'y')
    word = word.replace('9(*9(', 'e')
    word = word.replace('7!', 'he')      
    word = word.replace('%4%', ' a')
    return word
    
word_encrypted = encrypt(sentence)
word_decrypted = decrypt(word_encrypted)

len_difference = len(word_encrypted) - len(sentence)

print()
print("Encrypted as ==>", word_encrypted)
print("Difference in length ==>", len_difference)
print("Deciphered as ==>", word_decrypted)


if(word_decrypted == sentence) :
    print("Operation is reversible on the string.")
else :
    print("Operation is not reversible on the string.")





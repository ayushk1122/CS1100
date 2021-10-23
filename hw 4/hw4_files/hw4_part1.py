# -*- coding: utf-8 -*-
"""
Spyder Editor
This program determines the strength of a password using a set of different criteria 
It utilizes loops, conditionals, and functions to accomplish its outcome
author: Ayush Krishnappa
"""
import hw4_util

password = input("Enter a password => ").strip()
print(password)

"""
This function uses the length of the password and gives it a score 
Takes the password as the input and returns the score as an output
Prints a update statement anytime the score changes
"""
def length (password):
    score = 0
    if (len(password) == 6 or len(password) == 7):
        score += 1
        print("Length: +1")
    elif (len(password) >= 8 and len(password) <= 10):
        score += 2
        print("Length: +2")
    elif (len(password) > 10):
        score += 3
        print("Length: +3")
    return score

"""
This function updates the score based off the number of upper or lower case letters
Password as input score as output along with update statements for score changes
"""
def case (password):
    score = 0
    lower = 0
    upper = 0
    
    for char in password:
        if (char.isupper()):
            upper += 1
        elif (char.islower()):
            lower += 1
    
    if (upper >= 2 and lower >= 2):
        score += 2
        print("Cases: +2")
    elif (upper >= 1 and lower >= 1):
        score += 1
        print("Cases: +1")
        
    return score

"""
This function gives a score based off the number of numerical digits in a password
Takes password as input score as output 
"""
def digits (password):
    score = 0
    digits = 0
    
    for char in password:
        if (char.isnumeric()):
            digits += 1
    
    if (digits >= 2):
        score += 2
        print("Digits: +2")
    elif (digits >= 1):
        score += 1
        print("Digits: +1")
    
    return score

"""
This function gives the password a score based off special characters the password may have
prints a different statement based on which set of characters is included 
takes the password as an input and returns score as an output
"""
def punctuation (password):
    score = 0
    ## adds the counts together to account for all characters 
    if ((password.count('!') + password.count('@') + password.count('#') + password.count('$')) > 0):
        score += 1
        print("!@#$: +1")
    if ((password.count('%') + password.count('^') + password.count('&') + password.count('*')) > 0):
        score += 1
        print("%^&*: +1")
    return score

"""
This function determines if a password resembles a New York license plate based off its structure
Takes password as input and returns score as output
"""
def ny_license (password):
    score = 0
    ## uses nested if to make sure both conditions are met 
    if (password[0].isalpha() and password[1].isalpha() and password[2].isalpha()):
        if(password[3].isnumeric() and password[4].isnumeric() and password[5].isnumeric() and password[6].isnumeric()):
            score -= 2
            print("License: -2")
    return score

"""
This function determines if the password is a common one by looping through a list of 100 common passwords
Takes password as input score as output
"""
def common (password):
    score = 0
    ## uses lower to avoid case sensitivity
    password = password.lower()
    ## uses hw4_util module to get the 100 common passwords as a list
    common_list = hw4_util.part1_get_top()
    
    ## for each loop to compare each common password to the input password
    for passcode in common_list:
        if (passcode == password):
            score -= 3
            print("Common: -3")
    
    return score

"""
This function generates the output for the final statistics about the password
Takes the password as the input and returns nothing, prints instead
"""
def output (password):
    ## while calculating total score also prints update statements as well in method calls
    total_score = length(password) + case(password) + digits(password) + punctuation(password) + ny_license(password) + common(password)
    print("Combined score: {:d}".format(total_score))
    if (total_score <= 0):
        print("Password is rejected")
    elif (total_score == 1 or total_score == 2):
        print("Password is poor")
    elif (total_score == 3 or total_score == 4):
        print("Password is fair")
    elif (total_score == 5 or total_score == 6):
        print("Password is good")
    elif (total_score >= 7):
        print("Password is excellent")

output(password)

# -*- coding: utf-8 -*-
"""
Created on Wed Nov 10 14:10:02 2021

@author: Ayush
"""

from Date import Date
month_names = [ '', 'January', 'February', 'March', 'April', 'May', 'June', 'July',\
                    'August','September', 'October', 'November', 'December' ]
    
birthday_file = 'birthdays.txt'

def birthdays (file):
    birthdays = []
    for line in open(file):
        birthday = line.split(' ')
        year = int(birthday[0].strip())
        month = int(birthday[1].strip())
        day = int(birthday[2].strip())
        birthdays.append(Date(year, month, day))
        
    return birthdays
        
        
        
birthdays = birthdays(birthday_file)

earliest = birthdays[0]
latest = birthdays[0]
for date in birthdays:
    if (date < earliest):
        earliest = date
    if (date > latest):
        latest = date
        

month_counts = []
counter = 0
for i in range (len(month_names)):
    counter = 0
    for date in birthdays:
        if (date.month == i):
            counter += 1
    month_counts.append((counter, i))
    
month_counts.sort(reverse = True)
print(earliest)
print(latest)
print('The name of the month with the most birthdays is ' + month_names[month_counts[0][1]]) 

    
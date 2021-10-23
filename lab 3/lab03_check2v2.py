"""
This is a reconstruction of the lab03_check2 function, uses one function to return the same 
output instead of repeating code.

Author: Ayush Krishnppa 

"""

def calc_skew (name, time1, time2, time3, time4, time5) :
    name = str(name)
    time1 = int(time1)
    time2 = int(time2)
    time3 = int(time3)
    time4 = int(time4)
    time5 = int(time5)
    avg = (time1 + time2 + time3 + time4 + time5) / 5
    var = (time1-avg)**2 + (time2-avg)**2 + (time3-avg)**2 + (time4-avg)**2 + (time5-avg)**2
    var /= 5
    skew = (time1-avg)**3 + (time2-avg)**3 + (time3-avg)**3 + (time4-avg)**3 + (time5-avg)**3
    skew /= 5
    skew = skew/var**3**0.5
    output = (name + "'s" + " running times have a skew of {:0.2f}").format(skew)
    return output

def calc_stats (name, time1, time2, time3, time4, time5) :
    name = str(name)
    time1 = float(time1)
    time2 = float(time2)
    time3 = float(time3)
    time4 = float(time4)
    time5 = float(time5)
    minimum = int(min(time1, time2, time3, time4, time5))
    maximum = int(max(time1, time2, time3, time4, time5))
    total = time1 + time2 + time3 + time4 + time5
    average = (total - (minimum + maximum)) / 3
    output = (name + "'s" + " stats-- min: {:d}, max: {:d}, avg: {:0.1f}").format(minimum, maximum, average)
    print(output)


print(calc_skew('Stan', 34, 34, 35, 31, 29))
print(calc_skew('Kyle', 30, 31, 29, 29, 28))
print(calc_skew('Cartman', 36, 31, 32, 33, 33))
print(calc_skew('Kenny', 33, 32, 34, 31, 35))
print(calc_skew('Bebe', 27, 29, 29, 28, 30))

print()

calc_stats('Stan', 34, 34, 35, 31, 29)
calc_stats('Kyle', 30, 31, 29, 29, 28)
calc_stats('Cartman', 36, 31, 32, 33, 33)
calc_stats('Kenny', 33, 32, 34, 31, 35)
calc_stats('Bebe', 27, 29, 29, 28, 30)
""" 
    This is the skeleton to demonstrate how to put Lab 10 together. 
    It provides an example to show the use of doctest. Note the function,
    addone(x) presented below has an additional 4 lines after 
    the normal function description. The lines beginning with '>>>'
    indicate examples of how the function can be called, and 
    the lines immediately after represent the expected return
    from the call. So, for example, 'addone(1)' should return '2'
    and 'addone(0) should return 1. These lines provide examples
    for a potential user of the lab10 module, but more importantly
    for this lab, they work with the doctest module to allow us to
    do automated testing. 
    
    Look at the file 'test_driver.py' for an example of how to use
    this testing information. Then come back here and change 
    the answer for one or both of the addone examples to 
    an incorrect value and run the testing again to see how a failing
    test is reported.
"""
"""
def addone(x):
    '''
    addone(x) returns 1 more than
    the value x passed in.

    >>> addone(1)
    2
    >>> addone(0)
    1
    '''
    return x+1
"""
def closest1 (l1):
    '''

    Parameters
    ----------
    >>> closest1([1, 2, 7, 12, 19, 27, 34])
    (1, 2)
    
    >>> closest1([0.0, 3.7, 3.8, 4.7, 9.4])
    (3.7, 3.8)
    
    >>> closest1([1])
    (None, None)
    
    >>> closest1([1, 2, 3, 4, 5, 6, 7])
    (1, 2)
    
    >>> closest1([-1.2, 0.0, -0.3, -0.7, -1.7])
    (0.0, -0.3)
    
    '''
    if (len(l1) < 2):
        return (None, None)
    else:
        min_dist = l1[1] - l1[0]
        min_pair = (l1[0], l1[1])
        for i in range (len(l1)):
            for j in range (i + 1, len(l1)):
                if (abs(l1[j] - l1[i]) < min_dist):
                    min_dist = l1[j] - l1[i]
                    min_pair = (l1[i], l1[j])
        return min_pair
    
def closest2 (l1):
    '''

    Parameters
    ----------
    >>> closest2([1, 2, 7, 12, 19, 27, 34])
    (1, 2)
    
    >>> closest2([0.0, 3.7, 3.8, 4.7, 9.4])
    (3.7, 3.8)
    
    >>> closest2([1])
    (None, None)
    
    >>> closest2([1, 2, 3, 4, 5, 6, 7])
    (1, 2)
    
    >>> closest2([-1.2, 0.0, -0.3, -0.7, -1.7])
    (-0.3, 0.0)
    
    >>> closest2([7, 4, 5, 2, 0])
    (4, 5)
    
    '''
    if (len(l1) < 2):
        return (None, None)
    else:
        copy = l1.copy()
        copy.sort()
        min_dist = copy[1] - copy[0]
        min_pair = (copy[0], copy[1])
        for i in range (len(copy) - 1):
            if (abs(copy[i+1] - copy[i]) < min_dist):
                min_dist = copy[i+1] - copy[i]
                min_pair = (copy[i], copy[i+1])
        return min_pair

if __name__ == "__main__":
    pass

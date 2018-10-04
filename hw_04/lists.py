#Kyra Abbu

import random

#1
def build_random_list(size,max_value):
    """
    Parameters:
      size : the number of elements in the lsit
      max_value : the max random value to put in the list
    """
    l = [] # start with an empty list
    
    # make a loop that counts up to size
    i = 0
    while i < size:
        l.append(random.randrange(0,max_value))
        # we could have written this instead of the above line:
        # l = l + [random.randrange(0,max_value)]
        i = i + 1
    return l

#test
print('Build Random List Function:')
print('Random List 1:', build_random_list(10,50))
print('\nRandom List 2:', build_random_list(100,100))
print('\nRandom List 3:', build_random_list(25,13))
print('\nRandom List 4:', build_random_list(100,1000))

#2
def locate(l,value):
    """
    This routine should accept a list as the first parameter
    and a value for the second. The function will look for
    value in the list and return it’s index. Return -1 if value
    isn’t in the list. 
    """
    i = 0
    while i <= len(l):
        if value not in l: #if not found, program ends here
            x = 'Not Found: ' + str(-1)
            return x
        if value in l: 
            pass #does nothing
        if l[i] == value:
            x = 'Index: ' + str(i)
            return x
        else:
            i+=1
        
#test
print('\nLocate Function:')
print('List 1 ', locate(build_random_list(10,50),14))
print('\nList 2 ', locate(build_random_list(100,100),21))
print('\nList 3 ', locate(build_random_list(25,13),1))
print('\nList 4 ', locate(build_random_list(100,1000),9999))
    
#3    
def count(l,value):
    """
    This routine should accept a list as the first parameter and
    a value for the second. It should return the number of times
    value appears in the list l
    """
    counter = 0
    i = 0
    while i < len(l):
        if l[i] == value:
            counter = counter + 1
        else:
            counter = counter           
        i = i + 1           
    return counter       
        
#test
print('\nCount Function:')
print('List 1 ', 'Count:',count(build_random_list(10,50),14))
print('\nList 2 ', 'Count:',count(build_random_list(100,100),21))
print('\nList 3 ', 'Count:',count(build_random_list(25,13),1))
print('\nList 4 ', 'Count:',count(build_random_list(100,1000),9999))
    

    
#4  
def reverse(l):
    """
    This function should accept a list as its parameter. It will
    build and return a new list which has the same elements as the
    original but with the values reversed.
    """
    
        
#5   
def isIncreasing(l):
    """
    This function should accept a list as its parameter. It will
    return True if the list is strictly increasing, that is starting
    with the first element, each successive element is greater than
    the previous. For example, the list 1,5,10,11,13 is increasing
    while 1,5,3,6 and 1,4,4,6 are not.
    """

#6
def palindrome(l):
    """
    This function should return True if the list represents a palindrome
    and False otherwise. A list is a palindrome if it has the same elements
    left to right as it does right to left.
    """




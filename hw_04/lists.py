#Kyra Abbu
"""
Notes:
while loop: repeats a statement or group of statements while a
given condition is TRUE. It tests the condition before
executing the loop body.

for loop: executes a sequence of statements multiple times
and abbreviates the code that manages the loop variable.

break statement: terminates the loop statement and transfers
execution to the statement immediately following the loop.

continue statement: causes the loop to skip the remainder
of its body and immediately retest its condition prior to reiterating.

pass statement: the pass statement in is used when a statement is
required syntactically but you do not want any command or code to execute.
"""
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

#tests
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
        
#tests
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
countThis = [21, 21, 21, 26]

print('\nCount Function:')
print('List 1 ', 'Count:',count(build_random_list(10,50),14))
print('\nList 2 ', 'Count:',count(build_random_list(100,100),21))
print('\nList 3 ', 'Count:',count(build_random_list(25,13),1))
print('\nList 4 ', 'Count:',count(build_random_list(100,1000),9999))
print('\nList 5 ', 'Count:',count((countThis),21))
    

    
#4  
def reverse(l):
    """
    This function should accept a list as its parameter. It will
    build and return a new list which has the same elements as the
    original but with the values reversed.
    """
    print('\nOld List:', l)
    length = len(l)
    new_length = length
    new_list = []           
 #   i = 0
 #   while i <= len(l):
 #   if i != len(new_list):
    for element in l:
            new_length = new_length - 1
            item = l[new_length]
            new_list.append(item)
            #i+=1
    return new_list
    
        
print("\nReverse Function:")
print("New List 1:", reverse(build_random_list(10,50)))
print("New List 2:", reverse(build_random_list(5,2)))
print("New List 3:", reverse(build_random_list(40,99)))
    
        
#5 ***
"""
return statement in for loops:
return applies to the function and happens to ***terminate the for loop
prematurely*** by primarily bringing an end to the function
"""

def isIncreasing(l):
    """
    This function should accept a list as its parameter. It will
    return True if the list is strictly increasing, that is starting
    with the first element, each successive element is greater than
    the previous. For example, the list 1,5,10,11,13 is increasing
    while 1,5,3,6 and 1,4,4,6 are not.
    """
    old_num = l[0] #previous value
    print("\nList:", l)
    for element in l: #scans all elements
        if element < old_num: #descending
            #element is the number after old_num
            return False #if conditions are met here, it will terminate program
        # this will then repeat until for loop scans all successive items
        old_num = element #reassign
    return True #will execute if false did not hinder execution

a = [1, 2, 3, 4, 5]
b = [1, 2, 3, 1, 2]

print('\nisIncreasing Function:')
print("Increasing?",isIncreasing(a))
print("Increasing?",isIncreasing(b))
print("Increasing?",isIncreasing(build_random_list(10,50)))
print("Increasing?",isIncreasing(build_random_list(100,999)))

#6 ***
def palindrome(l):
    """
    This function should return True if the list represents a palindrome
    and False otherwise. A list is a palindrome if it has the same elements
    left to right as it does right to left.
    """
    print("\nList:",l)
    i = 0
    for element in l:
        if element != l[i-1]:
            return False
        i = i - 1
    return True

            
k = [1, 2, 3, 6, 2, 1]
j = [1, 2, 3, 3, 2, 1]

#tests
print('\nPalindrome Function:')
print(palindrome(k))
print(palindrome(j))
print(palindrome(build_random_list(40,99)))
print(palindrome(build_random_list(10,24)))



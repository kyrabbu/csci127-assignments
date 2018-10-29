"""
1. Create a list of 100 items.
Each item should be a random value
between 1 and 10.

2. Write a routine max(l) which will
return the index of an element with
the largest value in the list.
It can be any occurrence.

3. Write a routine freq(l,val)
which will return the number of
times val appears in list l.

4. Write a routine mode(l)
which will return the mode of
the list (the item that appears
most frequently). If the list has
multiple modes, you an return any of them.
"""

import random

def build_list(size,max_value):
    i = 0
    l1 = []
    while i < size:
        l1.append(random.randrange(0,max_value))
        i += 1
    return l1

def max(list):
    lv = 0
    #print('\nIndex of Largest Value:', list)
    for i in range(1,len(list)):
        if list[i] > list[lv]:
            lv = i
    return lv

def freq(l,val):
    lf = 0
    for i in l:
        if val == i:
            lf = lf + 1
    return lf

#look at an item, and repeat with list
def mode(l):
    max_mode = 0
    final_value = 0
    for i in l: #range(len(l))
        current_mode = freq(l,i)  #linear opperation; loops through again; takes time
        if current_mode >= max_mode: 
            max_mode = current_mode 
            final_value = i
    return final_value

#tallies
#more efficient modes
        
#tests
l = build_list(100,11)
print(l)
print('Largest Value:',max(l))
print('Frequency:',freq(l,7))
print('Mode:', mode(l))
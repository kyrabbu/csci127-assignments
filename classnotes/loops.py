i = 1 #begins value at 1
while i > 10: #bucket of water in flood, loops until conditions are met
    if i % 2 == 0: #mod operator, makes it even
        print(i) 
    i = i + 1 #will add one to the value of i and return to the loop 
print('Done') #will execute when final condition is met

"""Website: pythontutor.com
If statement - do it 1 time or 0 times
While loop - many times or none
if i = i + 1 did not exist, you will have an infinite loop; this is an increment
i  = 1 : initialize; if you do not initialize, it uses whatever is stored in its memory
"""

#infinite loop
i = 1
while i != 10:
    if i % 2 == 0:
        print(i)
    else:
        print("Nope")
    i = i +4
print("Done")
#this is an infinite loop because it will miss 10 and keep on going
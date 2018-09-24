#Kyra Abbu
#Partner: Darren Liang
"""
Write a program that prints the numbers from 1 to 100.
But for multiples of three print “Fizz” instead of the
number and for the multiples of five print “Buzz”.
For numbers which are multiples of both three and five print “FizzBuzz”.
Count how many times program returned "FizzBuzz"
"""

def fizzbuzz(max_value):
    count = 0
    i = 1
    while i <= max_value:
        if (i % 5 == 0) and (i % 3 == 0): #checks if divisible by both
            count += 1 #counts how many times FizzBuzz occurs
            print("FizzBuzz")  
        elif i % 3 == 0: #must use elif so it scans this after "if"; checks if divisible by 3
            print("Fizz") 
        elif i % 5 == 0: 
            print("Buzz") #checks if divisible by 5
        else: #if not divisible by anything
            print(i)
        i = i + 1 #loops until it reaches max_value
    return "Count:" + str(count) #turns count into string so it concantenates with string

print(fizzbuzz(100)) #print prints return value, without print count will not appear

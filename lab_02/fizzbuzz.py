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
        if (i % 5 == 0) and (i % 3 == 0): #must go first so that 3 and 5 do not repeat 
            print("FizzBuzz")
            count +=1 #counts how many times FizzBuzz occurs
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)
        i = i + 1
    return print(count) #returns value of count

fizzbuzz(100)

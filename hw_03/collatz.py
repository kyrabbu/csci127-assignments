#Kyra Abbu
#Partner: Will Lu

"""
In the loop print out sequence return and print out the number of steps
Print "steps: #"
Even- divides n/2
Odd- 3n+1
repeats until n=1
"""

def collatz(n):
    print("Initial Value:", n) 
    i = 0
    while n != 1: #repeats until n is 1
        if n % 2 == 0: #even
            n = n//2
            print(n)
        else:
            n = (3*n)+1 #odd
            print(n)
        i += 1 #adds a step when repeated
    print('Steps:', i)
        
collatz(20)
collatz(21)

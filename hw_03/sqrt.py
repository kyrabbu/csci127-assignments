#Kyra and Will
from random import randint  #import to generate random integer

def mysqrt(number):
    print("Guess the square root of", number,":")
    guess = randint(1, number) #generates random number
    previousGuess = 0 #stores value under while
    numberOfGuesses = 0 #counts loop times
    while previousGuess != guess:
        print(guess)
        previousGuess = guess #replaces value of initial previousGuess
        guess = (guess + number/guess) / 2       
        numberOfGuesses+=1
    print("Number of guesses: ", numberOfGuesses)


mysqrt(1000)
mysqrt(9)
mysqrt(16)
mysqrt(10000)
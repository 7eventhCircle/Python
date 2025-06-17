import sys
import random
import os
import string

i = 3


while i > 0:
    i = i - 1
    random_number = random.randint(1, 100)

# this allows the user to make a guess at what the random number is.
    guess = int(input('guess a number between 1-100: '))

    if 0 <= guess <= 100:

        if guess < random_number:
            print ('your guess is to low. you have ' ,i, 'chances left.')
    
        elif guess > random_number:
            print ('your guess is to high.' ,i, 'chances left.')

        elif guess == random_number:
            print ('you guess the number correctly!')
            break

    else:
        print('you can only enter a number between 1-100. Please try again.')
        break
    
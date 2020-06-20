'''This program is a number guessing game, a user will input a guess and the program will see if they are right.'''
from random import randint
from time import sleep

def get_user_guess():
  guess = int(input('Guess a number: '))
  return guess

def roll_dice(number_of_sides):
  first_roll = randint(1,number_of_sides)
  second_roll = randint(1,number_of_sides)
  max_val = number_of_sides * 2
  print ('The maximum value is ',max_val)
  user_guess = get_user_guess()
  if user_guess > max_val:
    print ('Your guess is more than the maximum allowed value, Please try again')
  else:
    print ('Rolling...')
    sleep(2)
    print (first_roll)
    sleep(1)
    print (second_roll)
    sleep(1)
    total_roll = first_roll + second_roll
    print (total_roll)
    print ('Result...')
    sleep(1)
    if user_guess == total_roll:
      print ('You guess the correct number, you win!')
    else:
        print ('Your guess was incorrect, you lost.')
    
roll_dice(6)
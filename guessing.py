# Richella O'Driscoll 2018-02-27
# Guessing Game

from random import randint


target = randint(1, 100)
guess = 101

print("Guess a number between 1 and 100:")
while guess != target:
    guess = int(input("Please enter your guess:"))
    if guess == target:
        print("Well Done! You guessed correctly!")
    elif guess < target:
        print ("Too Low!")
    else:
        print("Too High!")
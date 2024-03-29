#imports the ability to get a random number (we will learn more about this later!)
from random import *

#Generates a random integer.
aRandomNumber = randint(1, 20)
guesses = 0
# For Testing: print(aRandomNumber)
while guesses < 3:
	guess = input("Guess a number between 1 and 20:")
	if not guess.isnumeric(): # checks if a string is only digits 0 to 9
		print("That's not a positive whole number, try again!")
	else:
		guess = int(guess) # converts a string to an integer
		if aRandomNumber > guess:
			print("Guess a higher number")
			guess += 1
			continue

		elif aRandomNumber < guess:
			print("Guess a lower number")
			guess += 1
			continue

		else:
			print("CORRECT")
			guesses = 3

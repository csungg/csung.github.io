#imports the ability to get a random number (we will learn more about this later!)
from random import *

#Create the list of words you want to choose from.
aList = [0, 1]

#Generates a random integer.

FastFoods = ["McDonalds", "Wendys", "Five Guys", "Burger King"]
aRandomIndex = randint(0, len(FastFoods)-1)
print(len(FastFoods))
print(FastFoods[aRandomIndex])

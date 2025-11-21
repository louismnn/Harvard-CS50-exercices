import random

# square brackets indicate a list
coin = random.choice(["heads", "tails"])

print(coin)

# "from" is to import module in py but it's more specific than import
from random import choice
# will loads all the function called choice into workplace

random.randint(1, 10) # will return a number between 1 and 10 inclusive
number = random.randint(1, 10)
print(number)

cards = ["jack", "queen", "king"]
random.shuffle(cards)
# will shuffle all the cards
for card in cards:
    print(card)

print(random.choice(cards, k=2, weights = [40, 30, 30]))
# K=2 is for the number of cards I want to choice, default is 1
# weight is to weight the probability

import statistics

print(statistics.mean([100, 90]))

# sys for system
import sys

sys.argv # list of the command line, for exemple sys.argv[2] will print the third element of the command line

try:
    print("Hello, my name is", sys.argv[1])
except IndexError:
    print("Too few arguments")

if len(sys.argv) < 2:
    print("Too few arguments")
elif len( sys.argv) > 2:
    print("Too many arguments")
else:
    print("Hello, my name is", sys.argv[1])

sys.exit() # Will exit the program
# [1:-1] using a negative number have the effect to count in the other direction
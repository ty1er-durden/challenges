"""
Write a 1-player 'dice roll' game.

The game should do the following:
(1) Prompt the user to choose a number
(2) Validate that the user’s choice is valid on a 6 sided dice
(3) Roll the dice and keep repeating the roll until the user’s guess is correct
(4) Advise the user of how many rolls it took and congratulate them if it was
    a better than average performance
"""
import random
import time

guess = -1
while not (guess >= 1 and guess <= 6):
    guess = int(input("What number do you want me to roll on my dice (1-6)? "))

roll = None
roll_count = 0
while roll != guess:
    roll = random.randint(1, 6)
    print(roll)
    roll_count += 1
    time.sleep(0.5)

# The probability of a single roll being right is the chance of it matching the
# dice (1/6).  To work out the total probability of rolling the correct number
# in rolls is the sum of :
#   - The probability of getting it on roll 1
#   - The probability of getting it on roll 2 (not getting it on roll 1 AND getting it on roll 2)
# Written mathematically:
#   1/6 + 5/6 * 1/6
# For an arbitrary number of rolls this is can be calculated using this loop:
p = 0
for n in range(0, roll_count):
    p += (5 / 6) ** n * 1 / 6

message = "It took " + str(roll_count) + " attempt(s) to roll a " + str(guess) + "."
# If there was a less than 50% chance then you were deemed to be lucky:
if p < 0.5:
    message += " Congratulations. You are one lucky punk!"
print(message)

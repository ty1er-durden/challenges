'''
This week’s challenge has now being uploaded to GitHub in to
https://github.com/ty1er-durden/challenges/blob/master/challenge7/n_green_bottles.py:
Write a program to generate the lyrics to help me sing my kid to sleep with
his favourite song.  Sometimes he likes to start at twenty green bottles,
other nights he might want 10 pink bottles.  My wife suffers from dyscalculia
so there are bonus points for avoiding numbers written as digits as in the
example below:
    Two green bottles sitting on the wall,
    Two green bottles sitting on the wall,
    And if one green bottle should accidentally fall,
    There’ll be one green bottle sitting on the wall.
    One green bottle sitting on the wall,
    One green bottle sitting on the wall,
    And if one green bottle should accidentally fall,
    There’ll be zero green bottles sitting on the wall.
HINTS
    - Use a function to generate the lyrics
    - Tackle a simple case first (3 green bottles)
    - IF YOU WANT MORE OF A CHALLENGE
        - Update your function to take arguments for the
          number of bottles and their colour
        - Make sure your bottles are pluralized correctly
    - IF YOU WANT EVEN MORE OF A CHALLENGE
        - Add a second function to convert digits to text
          HINT use a dictionary for the conversion*
*If you wanted to use really big numbers, take a look at 'number_to_words'
in this module:
https://pypi.python.org/pypi/inflect
'''


import inflect



def song(number,colour,bottle):
    num = p.number_to_words(number)
    remainder=number-1
    rem=p.number_to_words(remainder)
    print ("""{0} {1} bottles sitting on the wall,
    {0} {1} bottles sitting on the wall,
    And if one {1} bottle should accidentally fall,
    There’ll be {2} green {3} sitting on the wall.
    """.format(num,colour,rem,bottle))

number=int(input('How many bottles do you want?'))
colour=input('What colour do you want?')

p = inflect.engine()

for i in range(number,0,-1):
    if i > 1:
        bottle=p.plural('bottle')
        song(i,colour,bottle)
    else:
        bottle='bottle'
        song(i, colour, bottle)

"""
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
"""


def number_to_text(n):
    NUMBERS_TO_TEXT = {
        0: "zero",
        1: "one",
        2: "two",
        3: "three",
        4: "four",
        5: "five",
        6: "six",
        7: "seven",
        8: "eight",
        9: "nine",
        10: "ten",
        11: "eleven",
        12: "twelve",
        13: "thirteen",
        14: "fourteen",
        15: "fifteen",
        16: "sixteen",
        17: "seventeen",
        18: "eighteen",
        19: "nineteen",
        20: "twenty",
    }
    if n < 0:
        return "An unnatural number of "
    if n <= 20:
        return NUMBERS_TO_TEXT[n]
    if n > 20:
        return "Loads of "


def generate_lyrics(bottle_count=10, colour="green"):

    lyrics = "\n"

    for n in range(bottle_count, 0, -1):
        bottles = number_to_text(n).title()
        bottles_left = number_to_text(n - 1)
        bottles_plural = "s"
        bottles_left_plural = "s"
        if n == 1:
            bottles_plural = ""
        elif n == 2:
            bottles_left_plural = ""
        lyrics += (
            f"{bottles} {colour} bottle{bottles_plural} sitting on the wall,\n"
        )
        lyrics += (
            f"{bottles} {colour} bottle{bottles_plural} sitting on the wall,\n"
        )
        lyrics += f"And if one {colour} bottle should accidentally fall,\n"
        lyrics += f"There’ll be {bottles_left} {colour} bottle{bottles_left_plural} sitting on the wall.\n\n"

    return lyrics


print(
    generate_lyrics(
        int(input("How many bottles? ")), input("And what colour are they? ")
    ),
    end="",
)

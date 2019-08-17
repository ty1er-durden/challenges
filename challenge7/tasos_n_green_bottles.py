#requires installation of the inflect library (pip install inflect)

import inflect
p = inflect.engine()

x = int(input("Hello user. Please provide the number of bottles for the song: "))
print("\n")

while x > 0:
    y = p.number_to_words(x)
    print("  ", y.capitalize(), "green bottles sitting on the wall,")
    print("  ", y.capitalize(), "green bottles sitting on the wall,")
    print("   And if one green bottle should accidentally fall,")
    print("   There'll be",p.number_to_words(x-1),"green bottle sitting on the wall.\n")
    x = x - 1

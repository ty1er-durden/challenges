"""
Write a program that prints the alphabet forwards, then backwards and then
repeat 13 times.  You should end up with a 26x26 grid of letters like this:

    <- 26 ->

 ^  ABC..XYZ
 |  Z......A
    ........
26  ........
    ........
 |  A......Z
 v  ZYX..CBA

HINTS:
(1) Don’t type out the alphabet manually!
(2) Take a look at https://docs.python.org/3/library/functions.html#chr
"""
alphabet = [chr(i) for i in range(65, 91)]

print(chr(0))
for i in range(0, 13):
    for j in alphabet:
        print(j, end="")
    print("")
    for j in alphabet[len(alphabet) - 1 :: -1]:
        print(j, end="")
    print("")
print(chr(0))

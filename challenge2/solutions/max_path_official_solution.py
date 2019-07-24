"""
You are writing a program to download the Python installer from the internet on
a Windows PC.

In Windows the maximum length for a local path is 259 characters. An example
would be:
C:\Downloads\python-3.7.3-amd64.exe

Write a program to check that the download destination chosen by a the user of
your program does not exceed the maximum length.

HINTS:
(1) We have not covered 'if' and 'else' yet. It is possible to write the
program without using them.
(2) Take a look at https://docs.python.org/3/library/functions.html#len
"""
MAX_PATH = 259
path = input("Enter full path to download file to: ")
print(
    "Destination path is ",
    int(len(path) < 259) * "not ",
    "longer than ",
    MAX_PATH,
    " characters.",
    sep="",
)

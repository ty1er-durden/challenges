"""
Write a simple calculator program that accepts
two numbers, and then carries out a calculation
on them:

GUIDANCE:

 - It should support the use of decimal numbers
 - It should support:
    - Addition
    - Subtraction
    - Multiplication
    - Division
 - It should fail CLEANLY if a divide by ZERO is attempted
"""
SUPPORTED_OPERATORS = ["+", "-", "*", "/"]

n1 = float(input("Enter first number: "))
op = input(f"Enter operator (one of {SUPPORTED_OPERATORS}): ")
n2 = float(input("Enter second number: "))

if op not in SUPPORTED_OPERATORS:
    print(f"Unable to perform calculation.  I do not recognise the '{op}' operator.")
elif op == "/" and n2 == 0.0:
    print("Unable to perform calculation.  No calculater can divide by zero!")
else:
    sum = str(n1) + " " + op + " " + str(n2)
    print("The answer to", sum, "is", eval(sum))

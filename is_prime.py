#!/usr/bin/python3
"""
Program: is_prime.py
Decription: a small tool to determine if the given number is a prime or not
Author: Joachim Ziebs
Version: 0.0.1
Licence: GPL v3 or later
"""

# Imports
import sys


# is_prime
def is_prime(num):          # Let's take the easy ones out first.
    if num == 1:
        return True
    elif num == 2:
        return True
    elif num == 3:
        return True
    else:
        for div in range(2, int(num / 2) + 1):  # Number crunching. :)
            #print("Number: ", num, "divided by: ", div, "modulo: ",\
            # (num % div)) # if you want to see the numbers
            #print(".", end="")              # One dot per division.
            print(div)                      # Print divisor
            if num % div == 0:              # No rest, no prime.
                return False
        return True


# Main
def main():
    if len(sys.argv) >= 2:
        number = int(sys.argv[1])
    else:
        print("Usage: is_prime.py [number].")
        sys.exit(0)
    print()
    print("Calculating: ", number)
    if is_prime(number):
        print()
        print(number, " is a prime number.")
    else:
        print()
        print(number, " is not a prime number.")
    print()
    sys.exit(0)


    # Execute!
if __name__ == "__main__":
    main()

#!/usr/bin/python3
"""
Program: is_prime_product.py
Decription: a simple script to determine if a given\
 number is a product of two primes
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
            print(".", end="")  # One dot per division.
            if num % div == 0:   # No rest, no prime.
                return False
        return True


# is_product
def is_product(num):
    for count in range(2, int(num / 2) + 1):
        if num % count == 0:
            multi1 = num / count
            if is_prime(multi1):
                multi2 = num / multi1
                if is_prime(multi2):
                    return True, multi1, multi2
                else:
                    return False, 0, 0
            else:
                return False, 0, 0


# Main
def main(arguments):
    if len(arguments) >= 2:
        product = int(arguments[1])
    else:
        print("Usage: is_prime_product.py [number].")
        sys.exit(0)
    # Lets see if the given number is a prime itself
    if is_prime(product):
        print()
        print(product, "is a prime.")
    else:
        is_it, prime1, prime2 = is_product(product)
        if is_it:
            print()
            print(product, " is the product of two primes.")
            print("The primes are: ", int(prime1), " and ", int(prime2), ".")
            print()
        else:
            print()
            print(product, " is not the product of two primes.")
            print()

    sys.exit(0)


# Execute!
if __name__ == "__main__":
    main(sys.argv)

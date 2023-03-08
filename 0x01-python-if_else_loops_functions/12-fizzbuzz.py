#!/usr/bin/python3

# FizzBuzz function that prints numbers from 1 to 100 with special cases for multiples of 3 and 5
def fizzbuzz():
    for i in range(1, 101):
        # If i is a multiple of both 3 and 5, print "FizzBuzz"
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz", end=' ')
        # If i is a multiple of 3, print "Fizz"
        elif i % 3 == 0:
            print("Fizz", end=' ')
        # If i is a multiple of 5, print "Buzz"
        elif i % 5 == 0:
            print("Buzz", end=' ')
        # Otherwise, print i
        else:
            print(i, end=' ')

# Test the function
fizzbuzz()

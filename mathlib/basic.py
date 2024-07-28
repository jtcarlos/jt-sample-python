""" Module for basic math arithmetic """

def add(addend_one, addend_two):
    """ Adds the given two number """
    return addend_one + addend_two

def subtract(minuend, subtrahend):
    """ Subtracts the given two numbers """
    return minuend - subtrahend

def multiply(multiplicand, multiplicator):
    """ Multiplies the given two numbers """
    return multiplicand * multiplicator

def divide(quotient, dividend):
    """ Divides the given two numbers """
    try:
        return quotient / dividend
    except ZeroDivisionError:
        print("You may not divide by 0")
        return None

def mean(numbers):
    """ Finds the median given an array of numbers """
    return round(sum(numbers) / len(numbers), 2)

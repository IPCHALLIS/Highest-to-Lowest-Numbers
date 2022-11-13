"""
Given a string of space separated numbers, return the highest and lowest number.
Output string must be two numbers separated by a single space, and highest number is first.
"""
def high_and_low(nums):
    """This function returns the highest and lowest numbers in a space separated string."""

    htl = list(map(int,nums.split()))
    """list() and map() converts string characters to integers.
       split() replaces single space with commas."""

    return "'{} {}'".format(max(htl),min(htl))
    """use 2 braces with single space to parse max/min numbers from (htl)."""


print(high_and_low("1 2 3 4 5"))  # return "5 1"
print(high_and_low("1 2 -3 4 5")) # return "5 -3"
print(high_and_low("1 9 3 4 -5")) # return "9 -5"
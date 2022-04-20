import sys
from functools import lru_cache


def find_near_factors(a):
    """
    The method to find and return the near factors of a specific integer.
    :param a: the integer
    :return: a set of integers called factors
    """
    factors = set()
    for i in range(1, a + 1):
        factor = int(a / i)
        if factor != a:
            factors.add(factor)
    return factors


@lru_cache(maxsize=None)
def new_red_green_calc(int_a):
    """
    The method that calculates what colour a specific integer is.
    It uses memoization to cache any returned results so that while it uses recursion,
    if it has already worked out a result previously, it can return it straight from the
    cache without any calculations necessary.
    :param int_a: The integer to work out if it is red or green
    :return: 1 if green, -1 if red
    """
    factor_arr = list(find_near_factors(int_a))
    g_count = 0
    for j in factor_arr:
        if j == 1:
            g_count += 1
        else:
            g_count += new_red_green_calc(j)
    if g_count > 0:
        return -1
    else:
        return 1


def rg_printer(int_a, int_b):
    """
    The method to find and print the string of r's and g's for the integers between and including 2 integers
    :param int_a: the integer to start from
    :param int_b: the integer to end at
    :return: a string with the first int, second int and then a line of r's and g's
    """
    final_str = "{int_a} {int_b} ".format(int_a=int_a, int_b=int_b)
    for i in range(int_a, int_b + 1):
        rg_int = new_red_green_calc(i)
        if rg_int == 1:
            final_str = final_str + "g"
        else:
            final_str = final_str + "r"

    return final_str


"""
Input and Task Decision
If valid, work out and print output
Else, print "Bad Input: {input}"
example input: "1 10"
"""
for line in sys.stdin:
    input = line.strip()
    if input:  # Python trick - empty strings are 'false'
        # input = input("Please enter input: ")
        # print("Your selection: " + input)
        x = input.split()
        if len(x) == 2 and x[0].isdigit() and x[1].isdigit() and int(x[1]) >= int(x[0]) > 0:
            print(rg_printer(int(x[0]), int(x[1])))
        else:
            print("Bad Input: {input}".format(input=input))

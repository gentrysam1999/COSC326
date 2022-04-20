import sys
import os
import random
import functools


full_rg_array = []


def new_load_full_rg_array():
    for i in range(1, 100001):
        factor_arr = list(find_near_factors(i))
        g_count = 0
        for j in factor_arr:
            if j == 1:
                g_count += 1
            else:
                g_count += full_rg_array[j-1]
        if g_count > 0:
            full_rg_array.append(-1)
        else:
            full_rg_array.append(1)


@functools.lru_cache(maxsize=None)
def new_red_green_calc(int_a):
    factor_arr = list(find_near_factors(int_a))
    g_count = 0
    for j in factor_arr:
        if j == 1:
            g_count += 1
        else:
            g_count += new_red_green_calc(j - 1)
    if g_count > 0:
        return -1
    else:
        return 1


def find_near_factors(a):
    factors = set()
    for i in range(1, a+1):
        factor = int(a / i)
        if factor != a:
            factors.add(factor)
    return factors


def red_green_calc(int_a, int_b):
    rg_array = []
    for i in range(int_a, int_b + 1):
        if full_rg_array[i] == 1:
            rg_array.append("g")
        else:
            rg_array.append("r")
    rg_string = "".join(rg_array)
    final_string = "{int_a} {int_b} {rg_string}".format(int_a=int_a, int_b=int_b, rg_string=rg_string)
    return final_string


# Creates factorsRG.txt if it doesn't exist
# Else reads file and loads into array
original_stdout = sys.stdout
if not os.path.isfile('./factorsRG.txt'):
    with open('factorsRG.txt', 'w') as rg_file:
        sys.stdout = rg_file
        new_load_full_rg_array()
        for letter in full_rg_array:
            print(letter)
        sys.stdout = original_stdout
else:
    with open('factorsRG.txt', 'r') as rg_file:
        full_rg_array = rg_file.read().splitlines()
        full_rg_array = list(map(int, full_rg_array))


# TEST PRINT STATEMENTS to check if find_near_factors is working
for i in range(1, 21):
    print(find_near_factors(i))


# print(find_near_factors(13))
# print(find_near_factors(22))
# print(find_near_factors(23))
# print(find_near_factors(24))
# print(find_near_factors(25))
# print(find_near_factors(26))
# print(find_near_factors(27))
# print(len(find_near_factors(10000000)))
# print(sorted(find_near_factors(10000000)))
# print(len(find_near_factors(5000000)))
# print(sorted(find_near_factors(5000000)))




for line in sys.stdin:
    input = line.strip()
    if input:  # Python trick - empty strings are 'false'
        # input = input("Please enter input: ")
        # print("Your selection: " + input)
        x = input.split()
        if len(x) == 2 and x[0].isdigit() and x[1].isdigit() and int(x[0]) <= int(x[1]):

            print(red_green_calc(int(x[0]), int(x[1])))
        else:
            print("Bad Input: {input}".format(input=input))

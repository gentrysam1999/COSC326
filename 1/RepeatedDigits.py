import sys



def task_a(base, integer):
    """
    Method for Task A:
    Given a base b and an integer n finds the longest block of
    integers all having repeated digits in base b that are less than n.

    :param base: The base to use.
    :param integer: the integer that the longest block's integers must be less than.
    """
    # print("Task A " + base + " " + integer)

    # -1 so that it doesn't include the highest integer ("repeated digits in base b LESS THAN N")
    count = str(int(integer) - 1)
    blocksize = 0
    blocksize_arr = []
    start_int_arr = []
    integers = []
    while int(count) > 0:
        if repeat_digit_check(num_to_base(count, base)):
            blocksize += 1
            # print("integer: " + count + ", blocksize: " + str(blocksize))
        if not repeat_digit_check(num_to_base(str(int(count) - 1), base)) and blocksize > 0:
            blocksize_arr.append(blocksize)
            start_int_arr.append(int(count))
            blocksize = 0
        count = str(int(count) - 1)

    if blocksize > 0:
        blocksize_arr.append(blocksize)
        start_int_arr.append(int(count + 1))
        blocksize = 0
    # print(blocksize_arr)
    # print(start_int_arr)
    blocksize_arr = blocksize_arr[::-1]
    start_int_arr = start_int_arr[::-1]
    max_blocksize = 0
    final_string = "0 0"
    if len(blocksize_arr) > 0:
        max_blocksize = max(blocksize_arr)
        max_index = blocksize_arr.index(max_blocksize)
        final_string = "{start_int} {block_length}".format(start_int=start_int_arr[max_index],
                                                           block_length=blocksize_arr[max_index])
    print(final_string)
    return



def task_b(base1, base2):
    """
    Method for Task B:
    Given two bases, b and c, finds the smallest integer n which
    has repeated digits in both bases.

    :param base1: the first base.
    :param base2: the second base.
    """
    # print("Task B " + base1 + " " + base2)
    integer = 1
    repeated_bool = False
    while not repeated_bool:
        if repeat_digit_check(num_to_base(str(integer), base1)) and repeat_digit_check(
                num_to_base(str(integer), base2)):
            repeated_bool = True
        else:
            integer += 1
    print(integer)


# checks if int has repeated digits and returns boolean
def repeat_digit_check(digit_array):
    """
    Checks if an array of digits has any repeating numbers

    :param digit_array: array of digits
    :return: boolean with result of if the array did have repeating digits
    """
    repeat_bool = False
    for i in range(0, len(digit_array)):
        for j in range(0, len(digit_array)):
            if i != j:
                if digit_array[i] == digit_array[j]:
                    repeat_bool = True
    # print(repeat_bool)
    return repeat_bool





def num_to_base(n, b):
    """
    Method to convert decimal number to a new base.

    :param n: The decimal number to convert.
    :param b: The base to convert to.
    :return: An array with the digits of the converted number
    """

    # to convert from decimal to destination base:
    # divide the decimal with the base until the quotient is 0 and calculate the remainder each time.
    # the destination base digits are the calculated remainders
    # https://www.rapidtables.com/convert/number/base-converter.html?fbclid=IwAR38XgTeo_JihVijDUSfLDVpibJYRbjYZ9VnKYpGjw34gkq3GoTJYCxCCS4

    destination_base = []
    leftover = n

    # while Quotient isn't 0
    while leftover:
        # add remainder of decimal/base to array
        destination_base.append(int(leftover) % int(b))
        # set leftover quotient to be (itself/the base)
        leftover = int(leftover) / int(b)

    # # CHECKS THAT CAN BE UNCOMMENTED TO BE USED
    # # check that int is converted to an array of digits
    # print(str(digit_array))
    # # check that destination base is worked out (is backwards due to append)
    # print(str(destination_base))
    # # array needs to be reversed because append adds the new digits to the back of the array
    # print(destination_base[::-1])


    # # convert array to an integer (NOT NEEDED but keeping commented because it is useful code for other work)
    # individual_strs = [str(integer) for integer in destination_base[::-1]]
    # combination_str = "".join(individual_strs)
    # final_int = int(combination_str)
    # print(final_int)
    # return final_int

    if destination_base[len(destination_base) - 1] == 0:
        destination_base.pop()

    # Array needs to be reversed because numbers are appended in reverse order
    # print(destination_base[::-1])
    return destination_base[::-1]



"""
Input and Task Decision
A = base integer
B = base base
example input: "A 1 1"
"""
for line in sys.stdin:
    input = line.strip()
    if input:  # Python trick - empty strings are 'false'
        # input = input("Please enter input: ")
        # print("Your selection: " + input)
        x = input.split()

        if len(x) == 3 and x[1].isdigit() and x[2].isdigit():
            if x[0] == "A":
                task_a(x[1], x[2])
            elif x[0] == "B":
                task_b(x[1], x[2])
            elif x[0] == "C":
                num_to_base(x[1], x[2])
            else:
                print("Bad line: " + input)
        else:
            print("Bad line: " + input)

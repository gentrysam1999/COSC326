import sys

global isCorrect
isCorrect = False


def digit_check(digit_arr):
    """
    Checks array to see if the first item is either 'N' or 'L' and following items are valid integers
    :param digit_arr: array to check
    :return: boolean confirming if string is valid
    """
    try:
        for i in range(0, len(digit_arr) - 1):
            if i == 0:
                if not (digit_arr[i] == 'N' or digit_arr[i] == 'L'):
                    # print(str(digit_arr[i]) + "=False")
                    return False
            else:
                int(digit_arr[i])
        return True
    except ValueError:
        return False
    # x[1].isdigit() and x[2].isdigit() and x[3].isdigit()


def normal_calc(res, operations, prev_calc, num_array, index):
    """
    Recursively builds a string of operations until it has a valid set that allows the numbers to correctly equal the
    given result when worked out normally.
    :param res: The given result
    :param operations: The string of operators
    :param prev_calc: The previous calculation with the operators applied
    :param num_array: The array of numbers to apply the operators to
    :param index: the current index of recursive calls
    :return: Valid strings of operators or None
    """
    global isCorrect
    if isCorrect:  # if already correct then return None
        return
    if prev_calc == res and index == len(num_array):  # correct final answer checker
        isCorrect = True
        if len(operations) > len(num_array) - 1:
            operations = operations[:-1]
        return operations
    elif prev_calc > res or index >= len(num_array):  # incorrect final answer checker
        return

    # do calculation with next number and operator
    temp_total = prev_calc
    if index > 0:
        temp_str = num_array[0]
        for i in range(1, index+1):
            temp_str += operations[i-1]
            temp_str += num_array[i]
        temp_total = eval(temp_str)
        # print(temp_str)
        # print(temp_total)
    index += 1

    # build plus side of tree
    plus_str = operations + "+"
    plus_dir = normal_calc(res, plus_str, temp_total, num_array, index)
    # build multiply side of tree
    mult_str = operations + "*"
    mult_dir = normal_calc(res, mult_str, temp_total, num_array, index)

    # if plus returns a good string then use it
    if plus_dir is not None:
        return plus_dir
    # else if multiply returns a good string then use it
    elif mult_dir is not None:
        return mult_dir
    return  # if neither is good then return None



def l_r_calc(res, operations, prev_calc, num_array, index):
    """
    Recursively builds a string of operations until it has a valid set that allows the numbers to correctly equal the
    given result when worked out left to right.
    :param res: The given result
    :param operations: The string of operators
    :param prev_calc: The previous calculation with the operators applied
    :param num_array: The array of numbers to apply the operators to
    :param index: the current index of recursive calls
    :return: Valid strings of operators or None
    """
    global isCorrect
    if isCorrect:  # if already correct then return None
        return
    if prev_calc == res and index == len(num_array):  # correct final answer checker
        isCorrect = True
        if len(operations) > len(num_array)-1:
            operations = operations[:-1]
        return operations
    elif prev_calc > res or index >= len(num_array):  # incorrect final answer checker
        return

    # do calculation with next number and operator
    temp_total = prev_calc
    if index > 0:
        if operations[-1] == "+":
            temp_total += int(num_array[index])
        elif operations[-1] == "*":
            temp_total *= int(num_array[index])
    index += 1

    # build plus side of tree
    plus_str = operations+"+"
    # print(plus_str)
    plus_dir = l_r_calc(res, plus_str, temp_total, num_array, index)
    # build multiply side of tree
    mult_str = operations+"*"
    # print(mult_str)
    mult_dir = l_r_calc(res, mult_str, temp_total, num_array, index)

    # if plus returns a good string then use it
    if plus_dir is not None:
        return plus_dir
    # else if multiply returns a good string then use it
    elif mult_dir is not None:
        return mult_dir
    return  # if neither is good then return None



"""
Input and Task Decision
If valid, work out and print output
Else, print "{input} Invalid"
example input: "N 7 1 2 3"
"""
for line in sys.stdin:
    input = line.strip()
    if input:  # Python trick - empty strings are 'false'
        # input = input("Please enter input: ")
        # print("Your selection: " + input)
        x = input.split()
        result = int()
        new_x = []

        # create new array with right order
        if (x[0] == 'N' or x[0] == 'L') and x[1].isdigit():
            new_x.append(x[0])
            new_x.append(x[1])
            result = int(x[1])
        elif (x[1] == 'N' or x[1] == 'L') and x[0].isdigit():
            new_x.append(x[1])
            new_x.append(x[0])
            result = int(x[0])
        else:
            new_x = x
        for i in range(2, len(x)):
            new_x.append(x[i])
        # Check array is valid
        if digit_check(new_x):
            # set up new array with numbers to use (not including result)
            new_num_array = []
            for i in range(2, len(new_x)):
                if i != len(new_x) - 1:
                    new_num_array.append(new_x[i])
                else:
                    new_num_array.append(new_x[i])

            # set global isCorrect variable to false before running recursive methods
            isCorrect = False


            if new_x[0] == 'N':  # normal order of operations
                operations_to_print = normal_calc(result, "", int(new_num_array[0]),  new_num_array, 0)
                if operations_to_print is None:
                    print("{input} impossible".format(input=input))
                else:
                    str_to_print = new_num_array[0]
                    for i in range(1, len(new_num_array)):
                        str_to_print += " "+operations_to_print[i-1]+" "+new_num_array[i]
                    print("N {result} = {str_to_print}".format(result=result, str_to_print=str_to_print))


            elif new_x[0] == 'L':  # L to R order of operations
                operations_to_print = l_r_calc(result, "", int(new_num_array[0]), new_num_array, 0)
                if operations_to_print is None:
                    print("{input} impossible".format(input=input))
                else:
                    str_to_print = new_num_array[0]
                    for i in range(1, len(new_num_array)):
                        str_to_print += " "+operations_to_print[i-1]+" "+new_num_array[i]
                    print("L {result} = {str_to_print}".format(result=result, str_to_print=str_to_print))


        else:
            print("{input} Invalid".format(input=input))

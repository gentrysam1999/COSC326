import sys


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


# def normal_check():
#
#
#
# def l_r_check():



def normal_calc(index, return_string, res, num_array):
    """
        Works out if any normal calculations are valid
        :param return_string: the string to return
                                (due to recursiveness it needs to be an input so that it can be passed back down)
        :param res: the result that the equation needs to equal
        :param num_array: the array of numbers and operators
        :return: a string with good or bad equation
        """
    npi_str = str()
    numbers_past_index = int()
    if index != len(num_array) - 1:
        for indexNums in range(index + 1, len(num_array)):
            npi_str += num_array[indexNums]
        numbers_past_index = eval(npi_str)
    else:
        numbers_past_index = int(num_array[index])

    return_string = "{input} impossible".format(input=input)
    num_str = str()
    for token in num_array:
        num_str += token
    new_result = eval(num_str)
    # print(str(new_result) + " check " + str(res))
    if new_result == res:
        return_string = "N {res} = {num_str}".format(res=res, num_str=num_str)
    elif new_result + numbers_past_index <= res:
        for a in range(1, len(num_array), 2):
            if num_array[a] != ' * ':
                # print(a)
                temp_num_array = list(num_array)
                temp_num_array[a] = ' * '
                # print(temp_num_array)
                # print(num_array)

                if return_string == "{input} impossible".format(input=input):
                    return_string = normal_calc(a, return_string, res, temp_num_array)

    return return_string

def l_r_calc(index, return_string, res, num_array):
    """
    Works out if any left to right calculations are valid
    :param return_string: the string to return
                            (due to recursiveness it needs to be an input so that it can be passed back down)
    :param res: the result that the equation needs to equal
    :param num_array: the array of numbers and operators
    :return: a string with good or bad equation
    """
    return_string = "{input} impossible".format(input=input)
    num_str = str()
    npi_str = str()
    numbers_past_index = int()
    new_result = int(num_array[0])
    for b in range(2, len(num_array), 2):
        if b >= index != len(num_array) - 1:
            npi_str = str(numbers_past_index)
            npi_str += num_array[b - 1]
            npi_str += num_array[b]
            numbers_past_index = eval(npi_str)
        elif index == len(num_array) - 1:
            numbers_past_index = int(num_array[index])
        num_str = str(new_result)
        num_str += num_array[b - 1]
        num_str += num_array[b]
        new_result = eval(num_str)

    num_str = ""
    for token in num_array:
        num_str += token

    if new_result == res:
        return_string = "L {res} = {num_str}".format(res=res, num_str=num_str)
    elif new_result + numbers_past_index <= res:
        # print(new_result)
        for a in range(1, len(num_array), 2):
            if num_array[len(num_array) - 1 - a] != ' * ':
                # print(a)
                temp_num_array = list(num_array)
                temp_num_array[len(num_array) - 1 - a] = ' * '
                # print(temp_num_array)
                # print(num_array)
                if return_string == "{input} impossible".format(input=input):
                    return_string = l_r_calc(a, return_string, res, temp_num_array)

    return return_string


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

        if digit_check(new_x):
            # print("Good Input: {input}".format(input=input))

            # set up new array with pluses between numbers
            new_num_array = []
            for i in range(2, len(new_x)):
                if i != len(new_x) - 1:
                    new_num_array.append(new_x[i])
                    new_num_array.append(' + ')
                else:
                    new_num_array.append(new_x[i])
            # print(new_num_array)

            if new_x[0] == 'N':
                # normal order of operations
                # print("normal order")
                print(normal_calc(2, "", result, new_num_array))
            elif new_x[0] == 'L':
                # L to R order of operations
                print(l_r_calc(2, "", result, new_num_array))

        else:
            print("{input} Invalid".format(input=input))
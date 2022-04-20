# for i up to num of pegs
#   for each position of each array
#
#       check if peg position can jump left, yes? append
#       check if peg position can jump no, yes? append
start_array = [1, 1]
original_array = [start_array]
# print(original_array)

# test_arr=[0, 0, 0, 0, 0]
# test_arr.append(1)
# print(test_arr)

def check_jump_left(pos, check_left_arr):
    if pos == 0:
        return True
    elif pos == 1 and check_left_arr[pos - 1] == 0:
        return True
    elif check_left_arr[pos - 1] == 0 and check_left_arr[pos - 2] == 0:
        return True
    else:
        return False




def check_jump_right(pos, check_right_arr):
    # print(pos)
    if pos == len(check_right_arr)-1:
        return True
    elif pos == len(check_right_arr)-2 and check_right_arr[pos + 1] == 0:
        return True
    elif check_right_arr[pos + 1] == 0 and check_right_arr[pos + 2] == 0:
        return True
    else:
        return False



def jump_left(pos, arr_jump_left):
    if pos == 0:
        # print("{pos} : {arr_jump_left}".format(pos=pos,arr_jump_left=arr_jump_left))
        arr_jump_left[pos] = 0
        arr_jump_left.insert(0, 1)
        arr_jump_left.insert(0, 1)
        # print(arr_jump_left)
    elif pos == 1:
        # print("{pos} : {arr_jump_left}".format(pos=pos, arr_jump_left=arr_jump_left))
        arr_jump_left[pos] = 0
        arr_jump_left[pos - 1] = 1
        arr_jump_left.insert(0, 1)
        # print(arr_jump_left)
    else:
        # print("{pos} : {arr_jump_left}".format(pos=pos, arr_jump_left=arr_jump_left))
        arr_jump_left[pos] = 0
        arr_jump_left[pos - 1] = 1
        arr_jump_left[pos - 2] = 1
        # print(arr_jump_left)
    return arr_jump_left



def jump_right(pos, arr_jump_right):
    # print(pos)
    if pos == len(arr_jump_right) - 1:
        # print("{pos} : {arr_jump_right}".format(pos=pos, arr_jump_right=arr_jump_right))
        arr_jump_right[pos] = 0
        arr_jump_right.append(1)
        arr_jump_right.append(1)
        # print(arr_jump_right)
    if pos == len(arr_jump_right) - 2:
        # print("{pos} : {arr_jump_right}".format(pos=pos, arr_jump_right=arr_jump_right))
        arr_jump_right[pos] = 0
        arr_jump_right[pos + 1] = 1
        arr_jump_right.append(1)
        # print(arr_jump_right)
    else:
        # print("{pos} : {arr_jump_right}".format(pos=pos, arr_jump_right=arr_jump_right))
        arr_jump_right[pos] = 0
        arr_jump_right[pos + 1] = 1
        arr_jump_right[pos + 2] = 1
        # print(arr_jump_right)
    return arr_jump_right


for i in range(1, 8):
    new_array_of_arrays = []
    if len(original_array) == 1:
        arr = original_array[0]
        new_array_of_arrays.append(jump_left(0, arr))
        new_array_of_arrays.append(jump_right(0, arr))
    else:
        for arr in original_array:
            # print(arr)
            for pos in range(0, len(arr)):
                if arr[pos] == 1:
                    # print("checking pos {pos} for array {arr}".format(pos=pos, arr=arr))
                    if check_jump_left(pos, arr):
                        # print("Jumping Left")
                        # print(jump_left(pos, arr))
                        # print("jumping left for pos {pos} for array {arr} to be: {new_arr}".format(pos=pos, arr=arr, new_arr=jump_right(pos, arr)))
                        new_array_of_arrays.append(jump_left(pos, arr))

                    if check_jump_right(pos, arr):
                        # print("Jumping Right")
                        # print(jump_right(pos, arr))
                        new_array_of_arrays.append(jump_right(pos, arr))
                        # print("jumping right for pos {pos} for array {arr} to be: {new_arr}".format(pos=pos, arr=arr, new_arr=jump_right(pos, arr)))

    original_array = new_array_of_arrays
    print(original_array)
# for i in original_array:
#     print(i)

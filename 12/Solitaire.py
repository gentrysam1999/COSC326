pos_set = []


def jump_left(peg_arr, pos):
    # setup array with 2 0s on the ends
    for num in range(0, 2):
        if peg_arr[num] != 0:
            peg_arr.insert(0, 0)
            pos += 1
    # jump peg if it can
    # print(len(peg_arr))
    # print(pos)
    if peg_arr[pos-1] == 0 and peg_arr[pos-2] == 0:
        peg_arr[pos] = 0
        peg_arr[pos - 1] = 1
        peg_arr[pos - 2] = 1

    #  cleanup array so that it has no 0s on the ends
    # print(peg_arr)
    for num in range(0, 2):
        if peg_arr[0] == 0:
            peg_arr.pop(num)

    return peg_arr



def jump_right(peg_arr, pos):
    # setup array with 2 0s on the ends
    for num in range(0, 2):
        if peg_arr[len(peg_arr)-1-num] != 0:
            # peg_arr.insert(len(peg_arr)-1-i, 0)
            peg_arr.append(0)

    # jump peg if it can
    # print(len(peg_arr))
    # print(pos)
    if peg_arr[pos+1] == 0 and peg_arr[pos+2] == 0:
        peg_arr[pos] = 0
        peg_arr[pos + 1] = 1
        peg_arr[pos + 2] = 1

    #  cleanup array so that it has no 0s on the ends
    # print(peg_arr)
    for num in range(0, 2):
        if peg_arr[len(peg_arr)-1] == 0:
            peg_arr.pop(len(peg_arr)-1)

    return peg_arr


def already_exist_check(peg_arr):
    # print(peg_arr)
    # print(pos_set)
    if peg_arr in pos_set or peg_arr[::-1] in pos_set:
        # print("{peg_arr} already exists".format(peg_arr=peg_arr))
        return
    else:
        # print("added {peg_arr} to array".format(peg_arr=peg_arr))
        pos_set.append(peg_arr)
        return






for i in range(1, 8):
    pos_arr = []
    if i == 1:
        pos_arr.append(1)
        pos_set.append(pos_arr)
    else:
        for arr in pos_set:
            pos_arr = arr
            for j in range(0, len(pos_arr)):
                if pos_arr[j] == 1:
                    already_exist_check(jump_left(pos_arr, j))
                    already_exist_check(jump_right(pos_arr, j))
    # print(pos_set)

# for arr in pos_set:
#     print(arr)


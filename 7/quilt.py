# http://anh.cs.luc.edu/handsonPythonTutorial/graphics.html
from graphics import *
import sys

# set up window
window_size = 500
win = GraphWin(width=window_size, height=window_size)  # create a window
win.setCoords(0, 0, 10, 10)  # set the coordinates of the window; bottom left is (0, 0) and top right is (10, 10)
square_level_count = 1


def float_check(input_float):
    try:
        float(input_float)
        return True
    except ValueError:
        return False


def square_calc(scale, r, g, b):
    colour = color_rgb(r, g, b)

    point_1 = Point(1, 1)
    point_2 = Point(9, 9)
    square_details = [colour, point_1, point_2]


# scale, r, g, b
def square_printer(big_level_count, small_level_count, temp_1, temp_2):
    # print(big_level_count)

    small_level_count += 1
    print(small_level_count)
    scale = scale_arr[small_level_count]
    scaled_scale = (scale / sum(scale_arr)) * 10

    point_1_num = temp_1 + (1 / 2 * scaled_scale)
    point_2_num = temp_1 - (1 / 2 * scaled_scale)
    point_3_num = temp_2 + (1 / 2 * scaled_scale)
    point_4_num = temp_2 - (1 / 2 * scaled_scale)
    if big_level_count != len(colour_arr)-1:

        if small_level_count == len(colour_arr)-1:
            big_level_count += 1
            small_level_count = 0

        # top right
        square1 = Rectangle(Point(point_2_num, point_1_num), Point(point_1_num, point_2_num))
        square1.setFill(colour_arr[small_level_count])
        square1.draw(win)
        square_printer(big_level_count, small_level_count, point_2_num, point_1_num)
        square_printer(big_level_count, small_level_count, point_1_num, point_2_num)

        # bottom right
        square2 = Rectangle(Point(point_2_num, point_3_num), Point(point_1_num, point_4_num))
        square2.setFill(colour_arr[small_level_count])
        square2.draw(win)
        square_printer(big_level_count, small_level_count, point_2_num, point_3_num)
        square_printer(big_level_count, small_level_count, point_1_num, point_4_num)

        # bottom left
        square3 = Rectangle(Point(point_4_num, point_3_num), Point(point_3_num, point_4_num))
        square3.setFill(colour_arr[small_level_count])
        square3.draw(win)
        square_printer(big_level_count, small_level_count, point_4_num, point_3_num)
        square_printer(big_level_count, small_level_count, point_3_num, point_4_num)

        # top left
        square4 = Rectangle(Point(point_4_num, point_1_num), Point(point_3_num, point_2_num))
        square4.setFill(colour_arr[small_level_count])
        square4.draw(win)
        square_printer(big_level_count, small_level_count, point_4_num, point_1_num)
        square_printer(big_level_count, small_level_count, point_3_num, point_2_num)

        # big_level_count += 1
        # small_level_count = 1
    return



"""
Input and Task Decision
If valid, work out and print output
Else, print "Bad Input: {input}"
example input: "1.0 255 0 0"
"""
# square_arr = []
scale_arr = []
colour_arr = []
# square_final_arr = []
for line in sys.stdin:
    input = line.strip()
    if input:  # Python trick - empty strings are 'false'
        # input = input("Please enter input: ")
        # print("Your selection: " + input)
        x = input.split()
        if len(x) == 4 and float_check(x[0]) and x[1].isdigit() and x[2].isdigit() and x[3].isdigit():
            temp_list = [float(x[0]), int(x[1]), int(x[2]), int(x[3])]
            scale_arr.append(float(x[0]))
            colour_arr.append(color_rgb(int(x[1]), int(x[2]), int(x[3])))
            # square_arr.append(temp_list)
        else:
            print("Bad Input: {input}".format(input=input))

temp_point_1 = float()
temp_point_2 = float()

# (scale/(total of all scales)) * (window scale, atm it's 10)
# square_calc(square_arr[0], square_arr[1], square_arr[2], square_arr[3])
scale = scale_arr[0]
scaled_scale = (scale / sum(scale_arr)) * 10
point_1_num = 5 + (1 / 2 * scaled_scale)
point_2_num = 5 - (1 / 2 * scaled_scale)
square = Rectangle(Point(point_1_num, point_1_num), Point(point_2_num, point_2_num))
square.setFill(colour_arr[0])
square.draw(win)
temp_point_1 = point_1_num
temp_point_2 = point_1_num
temp_point_3 = point_2_num
temp_point_4 = point_2_num

square_printer(1, 0, temp_point_1, temp_point_2, temp_point_3, temp_point_4)

# old square stuff
# point_1_num = temp_point_1 + (1 / 2 * scaled_scale)
# point_2_num = temp_point_1 - (1 / 2 * scaled_scale)
# point_3_num = temp_point_2 + (1 / 2 * scaled_scale)
# point_4_num = temp_point_2 - (1 / 2 * scaled_scale)


# # top right
# square1 = Rectangle(Point(point_2_num, point_1_num), Point(point_1_num, point_2_num))
# # bottom right
# square2 = Rectangle(Point(point_2_num, point_3_num), Point(point_1_num, point_4_num))
# # bottom left
# square3 = Rectangle(Point(point_4_num, point_3_num), Point(point_3_num, point_4_num))
# # top left
# square4 = Rectangle(Point(point_4_num, point_1_num), Point(point_3_num, point_2_num))

# square1.setFill(colour_arr[i])
# square2.setFill(colour_arr[i])
# square3.setFill(colour_arr[i])
# square4.setFill(colour_arr[i])
# square1.draw(win)
# square2.draw(win)
# square3.draw(win)
# square4.draw(win)
# temp_point_1 = point_1_num
# temp_point_2 = point_2_num
win.getMouse()  # pause before closing

# final_printer(square_final_arr)

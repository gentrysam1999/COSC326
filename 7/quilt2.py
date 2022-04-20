# http://anh.cs.luc.edu/handsonPythonTutorial/graphics.html
from graphics import *
import sys

# set up window
window_size = 500
global_scale = 100
win = GraphWin(width=window_size, height=window_size, autoflush=False)  # create a window
win.setCoords(0, 0, global_scale,
              global_scale)  # set the coordinates of the window; bottom left is (0, 0) and top right is (100, 100)

global_square_arr = []


def float_check(input_float):
    """
    Checks to see if a string can be converted to a float
    :param input_float: the string to check
    :return: boolean saying whether it can or not
    """
    try:
        float(input_float)
        return True
    except ValueError:
        return False


def square_printer(small_counter, p1_x, p1_y, p2_x, p2_y):
    """
    recursively calculates all of the squares to print and adds them to a global square array
    along with the layer number that they should be on.
    :param small_counter: counts the layer that the cube is on
    :param p1_x: x value for point 1
    :param p1_y: y value for point 1
    :param p2_x: x value for point 2
    :param p2_y: y value for point 2
    :return: exits once small_counter is too big
    """
    if small_counter != len(scale_arr):

        scale = scale_arr[small_counter]
        scaled_scale = (scale / sum(scale_arr)) * (global_scale*0.9)
        leftleft = p1_x + (1 / 2 * scaled_scale)
        leftright = p1_x - (1 / 2 * scaled_scale)
        rightleft = p2_x + (1 / 2 * scaled_scale)
        rightright = p2_x - (1 / 2 * scaled_scale)
        upup = p2_y + (1 / 2 * scaled_scale)
        updown = p2_y - (1 / 2 * scaled_scale)
        downup = p1_y + (1 / 2 * scaled_scale)
        downdown = p1_y - (1 / 2 * scaled_scale)

        # top left square
        square1 = Rectangle(Point(leftleft, upup), Point(leftright, updown))
        square1.setFill(colour_arr[small_counter])
        square1.setOutline(colour_arr[small_counter])

        # top right square
        square2 = Rectangle(Point(rightleft, upup), Point(rightright, updown))
        square2.setFill(colour_arr[small_counter])
        square2.setOutline(colour_arr[small_counter])

        # bottom left square
        square3 = Rectangle(Point(leftleft, downup), Point(leftright, downdown))
        square3.setFill(colour_arr[small_counter])
        square3.setOutline(colour_arr[small_counter])

        # bottom right square
        square4 = Rectangle(Point(rightleft, downup), Point(rightright, downdown))
        square4.setFill(colour_arr[small_counter])
        square4.setOutline(colour_arr[small_counter])

        global_square_arr.append([small_counter, square1])
        global_square_arr.append([small_counter, square2])
        global_square_arr.append([small_counter, square3])
        global_square_arr.append([small_counter, square4])
        # square1.draw(win)
        # square2.draw(win)
        # square3.draw(win)
        # square4.draw(win)

        square_printer(small_counter + 1, leftleft, upup, leftright, updown)
        square_printer(small_counter + 1, rightleft, upup, rightright, updown)
        square_printer(small_counter + 1, leftleft, downup, leftright, downdown)
        square_printer(small_counter + 1, rightleft, downup, rightright, downdown)
    else:
        return


"""
Input and Task Decision
If valid, work out and print output
Else, print "Bad Input: {input}"
example input: "1.0 255 0 0"
"""
scale_arr = []
colour_arr = []
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
        else:
            print("Bad Input: {input}".format(input=input))

temp_point_1 = float()
temp_point_2 = float()

s1_scale = scale_arr[0]
s1_scaled_scale = (s1_scale / sum(scale_arr)) * (global_scale*0.9)
point_1 = (1 / 2 * global_scale) + (1 / 2 * s1_scaled_scale)
point_2 = (1 / 2 * global_scale) - (1 / 2 * s1_scaled_scale)
square = Rectangle(Point(point_1, point_1), Point(point_2, point_2))
square.setFill(colour_arr[0])
square.draw(win)

temp_point_1 = point_1
temp_point_2 = point_1
temp_point_3 = point_2
temp_point_4 = point_2

square_printer(1, temp_point_1, temp_point_2, temp_point_3, temp_point_4)

sorted_multi_list = sorted(global_square_arr, key=lambda x: x[0])
for i in sorted_multi_list:
    # print(i[1])
    i[1].draw(win)
win.update()
win.getMouse()



# test values in decreasing scale for input
# 1.0 255 0 0
# 0.5 0 255 0
# 0.25 0 0 255
# 0.125 255 0 0
# 0.0625 0 255 0
# 0.03125 0 0 255
# 0.015625 255 0 0

# test values with varying scale
# 1.0 255 0 0
# 2.0 0 255 0
# 0.8 0 0 255
# 4.0 255 0 0
# 3.5 0 255 0
# 0.8 0 0 255
# 0.1 255 0 0

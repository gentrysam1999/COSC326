import sys
import re

# the output needs to be:
# Two numbers - Latitude Longitude
#       Latitude - a number between -90.000000 and 90.000000
#           N = positive, S = negative
#       Longitude - a number between -180.000000 and 180.000000
#           E = positive, W = negative
print("Program Running")


def dms_convert(dms_array):
    print("dms converter")
    lat_long_arr = float()
    lat = float()
    long = float()
    if 8 <= len(dms_array) > 2:
        print(dms_array)
        string1 = dms_array[0] + dms_array[1] + dms_array[2] + dms_array[3]
        string2 = dms_array[4] + dms_array[5] + dms_array[6] + dms_array[7]
        dms_array = [string1, string2]
        print(dms_array)
    if len(dms_array) == 2:
        for i in dms_array:
            deg, minutes, seconds, direction = re.split('[°\'"]', i)
            if direction == 'W' or direction == 'E':
                lat = ((float(deg) + float(minutes) / 60 + float(seconds) / (60 * 60)) * (
                    -1 if direction == 'W' else 1))
            elif direction == 'N' or direction == 'S':
                long = ((float(deg) + float(minutes) / 60 + float(seconds) / (60 * 60)) * (
                    -1 if direction == 'W' else 1))
    lat_long_arr = [lat, long]
    return lat_long_arr


def normal_convert():
    print("normal converter")


def convert_digits(direction_str, direction_int):
    if direction_str == "S" or direction_str == "W" and direction_int > 0:
        direction_int = -direction_int
    return direction_int


"""
Input and Task Decision
If valid, work out and print output
Else, print "Bad Input: {input}"
example input: "50 S, 40 E"
"""
for line in sys.stdin:
    input_str = line.strip()
    if input_str:  # Python trick - empty strings are 'false'
        # input_str = input("Please enter input: ")
        # print("Your selection: " + input)

        # remove commas
        input_str = input_str.replace(',', '')
        # input_str = input_str.replace(' d ', '° ')

        # print(input_str)
        x = input_str.split()
        # print(x)

        # check if there is a space before
        # if 'E ' or 'W ' or 'N 'or 'S 'in input_str:


        # clean up array by removing un-needed values
        # for i in x:
        #     if not (any(char.isdigit() for char in input_str) or i == 'E', 'W', 'N', 'S'):
        #         x.remove(i)
        # print("Trimming string")
        # print(input_str)
        # print(x)

        if '°' or ' d ' in input_str:
            print(dms_convert(x))
        else:
            normal_convert()

        print("\n\n")

        # if len(x) == 2 and x[0].isdigit() and x[1].isdigit() and int(x[1]) >= int(x[0]) > 0:
        #     print("Good Input: {input}".format(input=input))
        # else:
        #     print("Bad Input: {input}".format(input=input))

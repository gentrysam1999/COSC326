import sys
import re
from geojson import Point, Feature, FeatureCollection, dump

features = []


# checks if there are 2 directions or no directions
def good_string_checker(string):
    """
    checks the most basic checks for the string:
    * no 2 lats or longs
    * no direction as well as operator
    * there is a space in between last direction and any sentence
    :param string: string to check
    :return: boolean determining if string is bad
    """
    good_str_count = 0
    lat_count = 0
    long_count = 0
    test_split_string = string.split()
    isInt = True
    try:
        # converting to integer
        int(test_split_string[1])
    except ValueError:
        isInt = False
    if not isInt:
        length = len(test_split_string[1])
        last_letter = test_split_string[1][length - 1]
        if not(last_letter == 'N' or last_letter == 'S' or last_letter == 'E'
               or last_letter == 'W' or last_letter == 'd' or
               last_letter == 'm' or last_letter == '\''):
            return False
    for i in range(0, len(string)):
        if string[i] == 'E' or string[i] == 'W' or string[i] == 'S' or string[i] == 'N':
            # make sure that there aren't 2 latitudes or 2 longitudes
            if string[i] == 'E' or string[i] == 'W':
                long_count += 1
            elif string[i] == 'N' or string[i] == 'S':
                lat_count += 1
            if lat_count > 1 or long_count > 1:
                return False

            # checks that if a direction is in the string then there are no signs/operators
            if '-' in string or '+' in string:
                return False
            # if direction is the last char in string
            if i == len(string) - 1:
                good_str_count += 1
            # elif direction is followed by a space
            elif string[i + 1] == ' ':
                good_str_count += 1
    if good_str_count == 2:
        return True
    elif good_str_count == 0:
        return True
    else:
        return False


def direction_sorter(string):
    """
    Removes directions and will add negative sign if needed
    then returns a new string with these number ordered latitude then longitude
    :param string: string to sort
    :return: the new string
    """
    str_holder = string
    new_string = str()
    feature_info = ""
    for i in range(0, len(string)):
        if string[i] == 'S' or string[i] == 'W':
            temp_arr = str_holder.split(string[i])
            # create new string with right ordering (lat, long)
            if string[i] == 'S':
                new_string = (("-" + temp_arr[0].lstrip()) + new_string)
            else:
                new_string += ("-" + temp_arr[0].lstrip())

            # update str_holder with the rest of the string
            if len(temp_arr) >= 2:
                str_holder = temp_arr[1]
            else:
                str_holder = temp_arr[0]

        elif string[i] == 'N' or string[i] == 'E':
            temp_arr = str_holder.split(string[i])
            # create new string with right ordering (lat, long)
            if string[i] == 'N':
                new_string = ((temp_arr[0]) + new_string)
            else:
                new_string += (temp_arr[0])

            # update str_holder with the rest of the string
            if len(temp_arr) >= 2:
                str_holder = temp_arr[1]
            else:
                str_holder = temp_arr[0]
    # if str_holder.isalpha():
    # print(str_holder + " " + str(str_holder.isalpha()))
    feature_info = str_holder
    # if feature_info != "":
    #     print("Feature Info " + feature_info)

    new_string += str_holder
    # if new_string == '':
    #     new_string = string
    # print(new_string)
    return new_string


def dms_convert(string):
    """
    converts strings from dms form to single number form if they need it
    will also convert string to an empty string if there are any words left in the string (the only ones that should
    exist will be in between the numbers or if the full string is words).
    :param string: string to try and convert
    :return: the newly converted string
    """
    lat = float()
    long = float()
    new_string = string
    string = string.replace('d', '°')
    string = string.replace('m', '\'')
    string = string.replace('s', '"')

    if string.lower().islower():
        new_string = ""
    else:
        if '"' in string:
            string_arr = string.split('"')
            for i in range(0, 2):
                deg, minutes, seconds = re.split('[°\']', string_arr[i])
                if i == 0:
                    lat = (float(deg) + float(minutes) / 60 + float(seconds) / (60 * 60))
                else:
                    long = (float(deg) + float(minutes) / 60 + float(seconds) / (60 * 60))
                    new_string = str(lat) + " " + str(long)

    return new_string


def find_last_num(string):
    """
    finds and returns the last number's index in a string
    :param string: the string to check
    :return: the index of the last number
    """
    index = 0
    for i in range(0, 10):
        # print(i)
        temp_index = string.rfind(str(i))
        if temp_index > index:
            index = temp_index
    # print(string + " " + str(index))
    return index


def final_printer(final_array, f_string):
    """
    The final check that will check if the final numbers fit between the values that they should (-90, 90 for lat,
    -180, 180 for long)
    :param final_array: the array that should be of length 2 (lat, long), if not then it is a bad input.
    :return: the final string to be printed
    """
    final_string = str()
    if len(final_array) == 2:
        lat = float(final_array[0])
        long = float(final_array[1])

        if -90 <= lat <= 90 and -180 <= long <= 180:
            # final_string = str(round(lat, 6)) + " " + str(round(long, 6))
            final_string = ("{:.6f} {:.6f}".format(lat, long))
            point = Point((lat, long))
            features.append(Feature(geometry=point, properties={"name": f_string}))
        else:
            final_string = "Bad Input: {input}".format(input=input_str)

    else:
        final_string = "Bad Input: {input}".format(input=input_str)
    return final_string


"""
Input and Task Decision
If valid, work out and print output
Else, print "Bad Input: {input}"
example input: "50 S, 40 E"
"""
# get each line
for line in sys.stdin:
    input_str = line.strip()
    if input_str:
        # remove commas
        input_str = input_str.replace(',', '')

        # first check
        if good_string_checker(input_str):
            # remove any directions from strings and '-' signs if needed (for S and W)
            updated_string = direction_sorter(input_str)
            last_num_index = find_last_num(updated_string)
            num_string = (updated_string[0: last_num_index + 1])
            feature_string = (updated_string[last_num_index + 1: len(updated_string)])
            # print("\n\noriginal string: " + updated_string)
            # print("num_string: " + num_string)
            # print("feature_string: " + feature_string)
            updated_string = dms_convert(num_string)

            x = updated_string.split()
            print(final_printer(x, feature_string))
        else:
            print("Bad Input: {input}".format(input=input_str))

feature_collection = FeatureCollection(features)
with open('sams_file.geojson', 'w') as f:
    dump(feature_collection, f)

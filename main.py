import urllib.request
import json
import pathlib

def good_prompt_file(prompt = ''):
    file = input(prompt)
    while True:
        try:
            file = pathlib.Path(file)
            if file.is_file() != True:
                file = input("Please enter a correct input: ")
            else:
                print()
                return file
        except:
            print("boo")
            file = input("Please enter a correct input: ")

def good_prompt_str(prompt, *args):
    string = input(prompt)
    while string not in args:
        string = input("Please enter a correct input: ")
    print()
    return string

def good_prompt_int(prompt, value):
    #0 == Pos. or Zero
    #1 == Pos Only

    integer = input(prompt)
    while True:
        if integer.isdigit():
            integer = int(integer)
            if value == 0:
                if integer >= 0:
                    print()
                    return integer
            elif value == 1:
                if integer > 0:
                    print()
                    return integer

        integer = input("Please enter a correct input: ")


is_Nominatim_or_File = good_prompt_str("Will you be using a location name, or a pre-existing file as a center point for analysis?\nInput NOMINATIM or FILE: ", "NOMINATIM", "FILE")

if is_Nominatim_or_File == "NOMINATIM":
    location = input("Insert a location in order to use it as the center point: ")
    print()
else:
    location = good_prompt_file("Insert a file path in order to use the center point: ")

range_in_miles = good_prompt_int("Input an integer in miles, which will be the range that will be searched from the center point: ", 1)
threshold = good_prompt_int("Input an integer, which will be the threshold that will used to search for AQI levels at least as high as itself: ", 0)
max_locations = good_prompt_int("Input an integer, which will be the max locations that will be shown: ", 1)

aqi_or_file = good_prompt_str("Will you be using a call to PurpleAir's API, or a pre-existing file that contains a previous call to the PurpleAir API?\nInput PURPLEAIR or FILE: ", "PURPLEAIR", "FILE")
if aqi_or_file == "PURPLEAIR":
    #call to the api
    pass
else:
    pa_data = good_prompt_file("Insert a file path in order to use data from a call to PurpleAir's API: ")

reverse_geo = good_prompt_str("Will you be using Nominatim's API for reverse geocoding, or pre-existing files as calls to Nominatim's API?\nInput NOMINATIM or FILE: ", "NOMINATIM", "FILE")
if reverse_geo == "NOMINATIM":
    #call to api
    pass
else:
    reverse = []
    print("Please input until no longer prompted")
    for i in range(max_locations):
        reverse.append(good_prompt_file())


print(location, range_in_miles, threshold, max_locations, pa_data, reverse)
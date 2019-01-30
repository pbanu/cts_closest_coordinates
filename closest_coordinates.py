import json
import os
from math import sqrt


# Get .json file from directory
def read_coordinates_json(file_path):
    for root, dirs, files in os.walk(file_path):
        for file in files:
            if file.endswith(".json"):
                with open(os.path.join(root, file)) as f:
                    try:
                        coordinates = json.load(f)
                    except FileNotFoundError:
                        print("Unable to read file path")
    return coordinates


# Function to find closest coordinates
def sort_coordinate(coordinates, x, y):
    coordinates.sort(key = lambda p: sqrt((int(p["value"].split(',')[0]) - x)**2 + (int(p["value"].split(',')[1]) - y)**2))
    return coordinates


def main():
    # get directory path from user
    input_dir_path = input("Please enter input directory path:\n")
    coordinates = read_coordinates_json(input_dir_path)
    # get coordinates from user
    print("Please input origin (x,y)\n")
    x = input("x coordinate =  ")
    y = input("y coordinate =  ")
    ordered_coordinates = sort_coordinate(coordinates, int(x), int(y))
    print("Results")
    print(ordered_coordinates)


if __name__ == '__main__':
    main()


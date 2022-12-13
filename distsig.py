#! /usr/bin/env python3

# Day - Task

from sys import argv
# argv allows us to input a file name as a command line argument

def checkit():
    # check for a file name, if absent prompt user, otherwise run main function
    if len(argv) < 2:
        print("Really need a file name here!")
    else:
        main()

def main():
    # assign provided file to a variable, read only
    prod = open(argv[1], "r")

    # either show me the value or return it to be used further down the line
    print()
    # return 

if __name__ == "__main__":
    checkit()

#! /usr/bin/env python3

# Day1 - Task 1

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

    # variables for the upcooming calculations
    big = x = 0

    # iterate thru the file
    for line in prod:
        # remove those new lines
        line = line.strip("\n")
        # every time we reach a blank line, reset variable x
        if line == '':
            x = 0
        else:
            # add the current line to the value of x then compare to current largest value
            x += int(line) 
            if x > big:
                big = x

    # either show me the value or return it to be used further down the line
    print(big)
    # return big

if __name__ == "__main__":
    checkit()

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
    prod = open(argv[1], "r")

    big = x = 0

    for line in prod:
        line = line.strip("\n")
        if line == '':
            x = 0
        else:
            x += int(line) 
            if x > big:
                big = x

    print(big)
    return big

if __name__ == "__main__":
    checkit()

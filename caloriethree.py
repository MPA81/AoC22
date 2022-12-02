#! /usr/bin/env python3

# Day1 - Task 2

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

    # variable x calories per elf, list results tracks x totals
    x = 0
    results = []

    # iterate thru file
    for line in prod:
        # remove those new lines
        line = line.strip("\n")
        # every time we reach a blank line, add variable x to list results and reset x
        if line == '':
            results.append(x) 
            x = 0
        else:
            # add the current line to the value of x
            x += int(line) 

    # add the last variable x to list results and sort the list highest to lowest value
    results.append(x)
    results.sort(reverse=True)

    # add up the top 3 values
    total = results[0] + results[1] + results[2]

    # either print top 3 value total or return it for further use.
    print(total)
    # return total 

if __name__ == "__main__":
    checkit()

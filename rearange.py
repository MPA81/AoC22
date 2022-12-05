#! /usr/bin/env python3

# Day 3 - Task 1

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

    # list common for elements to be added, variable total for the sum of the values 
    common = []
    total = 0

    # iterate thru the file
    for line in prod:
        # remove new lines; check length of current line
        line = line.strip("\n")
        long = len(line)

        first = []
        second = []
        X = '' 

        counter = 0

        for i in line:
            if counter < (long / 2):
                first.append(i)
            else:
                second.append(i)
            counter += 1


        for j in first:
            if j in second and j != X:
                X = j
                common.append(j)

    for q in common:
        vali = ord(q)
        if vali > 97:
            total += (vali - 96)
        else:
            total += (vali - 38)

    # a = 97    z = 122    |    A = 65    Z = 90
                
    # either show me the value or return it to be used further down the line
    print(total)
    # return total

if __name__ == "__main__":
    checkit()

#! /usr/bin/env python3

# Day 6 - Task 1

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

    # a working list and a marker for the result 
    buffer = []
    marker = 0

    # set the length of the working list
    for j in range(4):
        buffer.append('')

    # get the line of trnasmision and establish its length
    for line in prod:
        long = len(line)
            
        # iterate thru the line and place elements in the working list
        for i in range(long):
            buffer[i % 4] = line[i]

            # once enought elements in the list turn list to set 
            if i > 3:
                checker = set(buffer)

                # check the length of the list versus length of set (set = unique elements)
                if len(checker) == len(buffer):
                    marker = i + 1

                    # print or return the result
                    print(marker)
                    return marker

if __name__ == "__main__":
    checkit()

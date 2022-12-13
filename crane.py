#! /usr/bin/env python3

# Day 5 - Task 1

from sys import argv
# argv allows us to input a file name as a command line argument

def checkit():
    # check for a file name, if absent prompt user, otherwise run main function
    if len(argv) < 2:
        print("Really need a file name here!")
    else:
        main()

# function for the crane movements
def crane(move, stack):
    # function specific counter
    county = 0

    # change list elements into variables to be used 
    nmb_of_mvs = int(move[1])
    source = int(move[3]) - 1
    destin = int(move[5]) - 1
 
    # remove boxes from top of stack loop 
    while county < nmb_of_mvs:
        # variable declared for value, then added to front of list
        x = stack[source].pop(0)
        stack[destin].insert(0, x)

        # variable to keep removal loop in check
        county += 1

    return stack


# function to turn first item in each list item as a string
def final(tsil):
    # local list for operations
    cuvant = [] 

    # loop thru list items and take first element only
    for i in tsil:
        cuvant += i[0]

    # return local list as a string
    return ''.join(cuvant)
       

def main():
    # assign provided file to a variable, read only
    prod = open(argv[1], "r")

    # lists declared: stacks and stacks new for elements, and directions for movements 
    stacks = [] 
    stacks_new = []
    directions = []

    # boolean set_up to switch from stacks part of file to directions section
    set_up = True
    # variable counter tracks line number and switches instructions in between sections
    counter = 0

    # iterate thru file line by line, remove new line character and establish line length
    for line in prod:
        line = line.strip("\n")
        long = len(line)

        # boolean set_up becomes false when crates organized (line 90), empty line after 
        if not set_up and line:
            # direction lines split at spaces into a list
            content = line.split(" ")
            directions.append(content)

        # iterate thru each line item and assign it to a variable
        for i in range(long):
            goofy = line[i]
  
            # in our first iteration we establish a list for stacks 
            if not counter:
                stacks.append(i)
                stacks[i] = []

            # boolean set_up permits us to diferentiate between stacks and directions
            if set_up:
                # only add labeled crates to the stacks
                if goofy.isalpha():
                    stacks[i] += goofy
                # once we reach provided stack number labels, boolean set_up becomes false 
                elif goofy == '1':
                    set_up = False

        # see label at line 61
        counter += 1

    # loop to remove un-necessary items from stacks list
    for j in stacks:
        if j != []:
            stacks_new.append(j)

    # iterate thru lines in directions and 
    for k in directions:
        stacks = crane(k, stacks_new)

    # either show me the value or return it to be used further down the line
    print(final(stacks))
    # return final(stacks)


if __name__ == "__main__":
    checkit()

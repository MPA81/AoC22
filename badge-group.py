#! /usr/bin/env python3

# Day 3 - Task 2 

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

    common = []
    working = []
    total = 0
    counter = 0

    group = []

    for x in range(3):
        group.append(x)
        group[x] = []

    for line in prod:
        line =  line.strip("\n")
        long = len(line)

        X = ''
        Y = ''

        for i in line:
            group[counter%3].append(str(i))

        for j in group[0]:
            if j in group[1] and j != X:
                X = j
                working.append(j)

        for q in working:
            if q in group[2] and q != Y:
                Y = q
                common.append(q)
    
        counter += 1

        if counter == 3:
            for z in range(3):
                group[z] = []
            working = []
            counter = 0

    # a = 97    z = 122    |    A = 65    Z = 90

    for q in common:
        vali = ord(q)
        if vali > 97:
            total += (vali - 96)
        else:
            total += (vali - 38)
                
    # either show me the value or return it to be used further down the line
    print(total)
    # return total

if __name__ == "__main__":
    checkit()

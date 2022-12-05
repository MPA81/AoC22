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

def inclusion(one, two):
        X = True
        one = one.split("-")
        two = two.split("-")

        a = int(one[0])
        b = int(one[1]) + 1
        c = int(two[0])
        d = int(two[1]) + 1

        for i in range(a,b):
            print(i)
            if i not in range(c,d):
                X = False

        return X
        
def main():
    # assign provided file to a variable, read only
    prod = open(argv[1], "r")

    contained = 0

    for line in prod:
        new = []

        line = str(line.strip("\n"))
        this = line.split(",")
        new.append(this[0])
        new.append(this[1])

        if new[0] != new[1]:
            if inclusion(new[0], new[1]):
                contained += 1

        if inclusion(new[1], new[0]):
            contained += 1
    
    # either show me the value or return it to be used further down the line
    print(contained)
    # return contained

if __name__ == "__main__":
    checkit()

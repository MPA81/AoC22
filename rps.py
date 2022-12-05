#! /usr/bin/env python3

# Day 2 - Task 1

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

    # lists: opp - opponent move, pla - player move
    opp = ['A', 'B', 'C']
    pla = ['X', 'Y', 'Z']

    # variable score will keep track of the current score value
    score = 0

    # loop thru the file line by line
    for line in prod:
        # variable x - opponents hand; variable y - player hand, indexed from lists for value
        x = opp.index(line[0])
        y = pla.index(line[2])

        # resolve edge cases: top hand loses to bottom hand
        if (x == 2) and (y == 0):
            score += 6 
        elif (x == 0) and (y == 2):
            score
        # once edge cases are resolved, player has higher hand +6, hands are equal +1
        elif y > x:
            score += 6
        elif x == y:
            score += 3
        # value added for a loss is 0, safe to ignore the only other option (player losing)

        # win or lose, player hand value + 1 added to score
        score += y + 1 

    # either show me the value or return it to be used further down the line
    print(score)
    # return score

if __name__ == "__main__":
    checkit()

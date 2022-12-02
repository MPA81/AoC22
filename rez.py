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

    # lists: opp - opponent move, rez - desired result, tba - result value
    opp = ['A', 'B', 'C']
    rez = ['X', 'Y', 'Z']
    tba = [0, 3, 6]

    # variable score will keep track of the curent score value
    score = 0

    # loop thru the file line by line
    for line in prod:
        # variable x - oponents hand; variable y - desired result, indexed from lists for value
        x = opp.index(line[0])
        y = rez.index(line[2])

        # option 1) result is a tie, we can add opponent hand value + 1 to score
        if y == 1:
            score += (x + 1)
        # option 2) result is a loss, two posibilities
        elif y == 0:
            # top hand looses to bottom value, 2 + 1 added to score
            if x == 0:
                score += 3
            else:
            # otherwise a loss implies our hand is -1 from opponent, result x - 1 + 1
                score += x 
        # option 3) winining is the only other possible outcome. Again two possibilities
        else:
            # opponent has the top hand, we win with bottom value, 0 + 1 added to score
            if x == 2:
               score += 1
            # otherwise a win implies our hand is + 1 from oponent, x + 1 + 1
            else:
               score += (x + 2)
       
        # list tba contains result values, added to variable score after each round 
        score += tba[y] 

    # either show me the value or return it to be used further down the line
    print(score)
    # return score

if __name__ == "__main__":
    checkit()

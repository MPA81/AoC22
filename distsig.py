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

    left = []
    right = []
    counter = 0 

    for line in prod:
        line = line.strip('\n')
        usage = line.split(',')

        print(usage)

        wrk = []
        cur = []
        counter = counter % 3
        #print(counter)

        for i in usage:
            if counter == 0 and i[1].isnumeric():
                print('eureka')

        #    if i:
        #        if i[0] == '[':
        #            if i[1] != ']':
        #                print()
        #                #cur.append(int(i[1]))
        #            else:
        #                wrk.append(cur)
        #                cur = []
        #        else:
        #            wrk.append(int(i))
        #    else:
        #        wrk.append(i)
        
        # print()

        #if counter == 0:
        #    left = wrk 
        #elif counter == 1:
        #    right = wrk
            #long = len(left)
            #rong = len(right)

        #for j in right:
            #print(j)
                
        counter += 1
        

    # either show me the value or return it to be used further down the line
    print()
    # return 

if __name__ == "__main__":
    checkit()

#!/usr/bin/python

import sys

#possibilities
#1
#[[1], [2], [3]]
#2
#[1,1], [1,2], [1,3], [2,1], [2,2], [2,3], [3,1], [3,2], [3,3]
#3
#[1,1,1], [1,1,2], [1,1,3], [1,2,1], [1,2,2], [1,2,3], [1,3,1], [1,3,2], [1,3,3], [2,1,1], [2,1,2], [2,1,3], [2,2,1], [2,2,2], [2,2,3], [2,3,1], [2,3,2], [2,3,3], [3,1,1], [3,1,2], [3,1,3], [3,2,1], [3,2,2], [3,2,3], [3,3,1], [3,3,2], [3,3,3]

#3
#9
#27
#
# 3^n possibilities

def rock_paper_scissors(n):

    def recurs(num, l):
        options = [['rock'], ['paper'], ['scissors']]

        if num > 0:
            #Multiplies the list in the right order, 2nd rec =  [[r], [r], [p], [p], [s], [s]]
            new_list = [l[x//3] for x in range(len(l)*3)]
            # print(f" num: {num},\n list: {l},\n new_list: {new_list} ")
            for i in range(0, len(new_list)):
                new_list[i] = new_list[i] + options[i%3]
            return(recurs(num-1, new_list))
        else:
            return l

    returned_list = recurs(n-1, [['rock'], ['paper'], ['scissors']])

    if n == 0:
        return [[]]
    else:
        return returned_list


if __name__ == "__main__":
    if len(sys.argv) > 1:
        num_plays = int(sys.argv[1])
        print(rock_paper_scissors(num_plays))
    else:
        print('Usage: rps.py [num_plays]')
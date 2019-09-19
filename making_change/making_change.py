#!/usr/bin/python

import sys

def making_change(amount, denominations, cache={}):
    # combinations = 0

    # if amount < 0:
    #     return 0
    # elif amount in cache:
    #     return cache[amount]
    # else:
    #     for i in range(0,len(denominations)):
    #         combinations += making_change(amount-denominations[i], denominations[i::], cache)

    cache = {
            0: 1
        }
    
    for c in denominations:
        for i in range(c, amount+1):
            if i in cache:
                cache[i] += cache[i-c]
            else:
                cache[i] = cache[i-c]

    return cache[amount]


if __name__ == "__main__":
    # Test our your implementation from the command line
    # with `python making_change.py [amount]` with different amounts
    if len(sys.argv) > 1:
        denominations = [1, 5, 10, 25, 50]
        amount = int(sys.argv[1])
        print("There are {ways} ways to make {amount} cents.".format(ways=making_change(amount, denominations), amount=amount))
    else:
        print("Usage: making_change.py [amount]")
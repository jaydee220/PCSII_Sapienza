#!/bin/python3

import sys
from collections import Counter, OrderedDict
import operator

if __name__ == "__main__":
    s = input().strip()
    counter = Counter(s)
    counter_sorted_vals = sorted(counter.items(), key=operator.itemgetter(0))
    counter_sorted = sorted(counter_sorted_vals, key=operator.itemgetter(1), reverse=True)
    for keys,values in counter_sorted[:3]:
            print (keys,values)

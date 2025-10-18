import bisect
import collections
import copy
import heapq
import itertools
import math
import string
import sys


def intInput():
    return int(sys.stdin.readline().rstrip())


def listIntInput():
    return list(map(int, sys.stdin.readline().rstrip().split()))


def strInput():
    return sys.stdin.readline().rstrip()


def ListStrInput():
    return list(sys.stdin.readline().rstrip().split())


lst = listIntInput()
print(lst[0] * lst[1])

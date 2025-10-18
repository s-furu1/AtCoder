import bisect
import collections
import copy
import heapq
import itertools
import math
import string
import sys
import numpy


def intInput():
    return int(sys.stdin.readline().rstrip())


def listIntInput():
    return list(map(int, sys.stdin.readline().rstrip().split()))


def strInput():
    return sys.stdin.readline().rstrip()


def ListStrInput():
    return list(sys.stdin.readline().rstrip().split())


A = listIntInput()
B = strInput()
cnt = 0
ans = ""
for i in range(len(B) - A[1]):
    rng = i + A[1]
    cnt2 = B.count(B[i:rng])
    if cnt < cnt2:
        cnt = cnt2
        if ans == "":
            ans = B[i:rng]
        else:
            ans += " " + B[i:rng]

print(cnt)
print(ans)

# 解けず。
# シンプルに重なり合った文字列の取得方法、カウント方法が思い浮かばず撃沈。
# 精進あるのみ

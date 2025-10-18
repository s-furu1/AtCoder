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
if A[3] >= A[1]:
    count = 0
    for i in range(A[3]):
        if i < A[1]:
            count += 1
        elif i - A[1] - A[2] < 0:
            continue
        elif (i + 1) % (A[1] + A[2]) > 0 and (i + 1) % (A[1] + A[2]) <= A[1]:
            count += 1
    print(A[0] * count)
else:
    print(A[0] * A[3])

# 時速{A[0]}で{A[1]}秒間走ったのちに{A[2]}秒間停止する高橋くんが動作を開始してから、{A[3]}秒後の時点で進んだ距離xを出力せよ、という問題。
# スタートからそのループ時点での秒数を数え、その秒数時点で停止状態でない場合はcountを1増やす、という考え方で解いた。
# 頭の中で整理するのにかなり時間がかかった。ただの算数問題のはずがfor文でちまちま（しかも要らない分岐まで入れて）やってしまった。反省。
# これを解くのに1時間も費やした。。

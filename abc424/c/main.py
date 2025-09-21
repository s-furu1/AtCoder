import sys


def input():
    return sys.stdin.readline().rstrip()


def main():
    N = int(input())
    learned = []
    for i in range(1, N + 1):
        a, b = map(int, input().split())
        if (a, b) == (0, 0):
            learned.append(i)
        elif (a in learned and b not in learned):
            learned.append(i)
        elif (b in learned and a not in learned):
            learned.append(i)
    print(len(learned))


if __name__ == '__main__':
    main()

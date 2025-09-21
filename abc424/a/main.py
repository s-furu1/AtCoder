import sys


def input():
    return sys.stdin.readline().rstrip()


def exam(a, b, c):
    if a == c or a == b or b == c or (a == b and b == c):
        return 'Yes'
    else:
        return 'No'


def main():
    a, b, c = map(int, input().split())
    answer = exam(a, b, c)
    print(answer)


if __name__ == '__main__':
    main()

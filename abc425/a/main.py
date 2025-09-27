import sys


def input():
    return sys.stdin.readline().rstrip()


def main():
    N = int(input())
    ans = 0
    for i in range(1, N + 1):
        if i % 2 == 1:
            ans += (-1 * (i ** 3))
        else:
            ans += (i ** 3)
    print(ans)


if __name__ == '__main__':
    main()

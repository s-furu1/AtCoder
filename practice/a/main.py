import sys


def input():
    return sys.stdin.readline().rstrip()


def main():
    # ここに回答を書いていく
    a = int(input())
    b, c = map(int, input().split())
    d = input()
    print(a + b + c, d)


if __name__ == '__main__':
    main()

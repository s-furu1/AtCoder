import sys


def input():
    return sys.stdin.readline().rstrip()


def main():
    N, M, K = map(int, input().split())
    l_empty = [0] * N
    answer = ""
    for _ in range(K):
        n, m = map(int, input().split())
        n -= 1
        l_empty[n] += 1
        if l_empty[n] == M:
            if answer == "":
                answer += str(n + 1)
            else:
                answer += " "
                answer += str(n + 1)
    print(answer)


if __name__ == '__main__':
    main()

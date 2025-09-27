import sys


def input():
    return sys.stdin.readline().rstrip()


def main():
    N = int(input())
    print(N)
    input_line = input().split()
    input_line = [int(number) for number in input_line]
    p_line = list(range(1, N + 1, 1))
    if len(input_line) != len(set(input_line)):
        print("Yes")
    else:
        print("No")
        return
    for i in range(1, N + 1):
        if input_line[i] == -1:
            key_data = set(input_line) ^ set(p_line)
            # input_line[i] == key_data{1}

        # for i in range(1, N + 1):

    print(key_data)

    print(p_line)


if __name__ == '__main__':
    main()

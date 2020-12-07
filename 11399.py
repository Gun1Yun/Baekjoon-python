import sys
In = sys.stdin.readline


def main():
    N = int(In())
    times = list(map(int, In().split()))
    times.sort()
    sum = 0
    for i in times:
        sum += N*i
        N -= 1
    print(sum)


main()

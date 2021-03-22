# 보물
import sys
In = sys.stdin.readline


def main():
    n = int(In())
    a = list(map(int, In().split()))
    b = list(map(int, In().split()))

    a.sort()
    b.sort()
    b.reverse()

    s = 0
    for i, j in zip(a, b):
        s += i*j

    print(s)


if __name__ == "__main__":
    main()

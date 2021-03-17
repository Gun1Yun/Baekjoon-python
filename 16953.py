# A -> B
import sys
In = sys.stdin.readline


def main():
    a, b = map(int, In().split())
    cnt = 0

    while True:
        if a == b:
            print(cnt + 1)
            break
        elif a > b:
            print(-1)
            break

        if b % 10 == 1:
            b = b // 10
        elif b % 2 == 0:
            b = b // 2
        else:
            print(-1)
            break

        cnt += 1


if __name__ == "__main__":
    main()

# 병든 나이트
# 2up, 1right
# 1up, 2right
# 1down, 2right
# 2down, 1right
import sys
In = sys.stdin.readline


def main():
    n, m = map(int, In().split())
    limit = 4

    if 2 < n:
        if m <= limit:
            print(m)
        elif limit < m <= limit+2:
            print(limit)
        else:
            print(m-2)
    else:
        if n == 2:
            if m < 3:
                print(1)
            elif m < 5:
                print(2)
            elif m < 7:
                print(3)
            else:
                print(4)
        else:
            print(1)


if __name__ == "__main__":
    main()

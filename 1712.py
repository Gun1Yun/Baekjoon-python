import sys
In = sys.stdin.readline


def main():
    A, B, C = map(int, In().split())
    if B < C:
        sales = A//(C-B) + 1
        print(sales)
    else:
        print(-1)


main()

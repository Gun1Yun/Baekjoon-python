# 주식
import sys
In = sys.stdin.readline


def main():
    tc = int(In())

    for _ in range(tc):
        n = int(In())
        stocks = list(map(int, In().split()))
        stocks.reverse()

        profit = 0
        now = stocks[0]

        for i in range(1, len(stocks)):
            if now > stocks[i]:
                profit += now - stocks[i]
            elif now < stocks[i]:
                now = stocks[i]

        print(profit)


if __name__ == "__main__":
    main()

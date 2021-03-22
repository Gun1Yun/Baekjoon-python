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

        # best = sorted(stocks, reverse=True)
        # i = 0

        # profit = 0
        # cnt = 0
        # last = 0
        # # 나머지
        # for stock in stocks:
        #     if stock == best[i]:
        #         profit += stock*cnt
        #         last = 0
        #         cnt = 0
        #         i += 1
        #         print('sell')
        #     else:
        #         profit -= stock
        #         last += stock
        #         cnt += 1
        #         print('buy')
        #         del best[b]

        print(profit)


if __name__ == "__main__":
    main()

import sys
In = sys.stdin.readline


def main():
    n = int(In())
    cnt_5 = n//5  # 5 최대 개수
    sum = 0

    while cnt_5 >= 0:
        tmp = n - 5*cnt_5
        if tmp % 3 == 0:
            sum = tmp//3 + cnt_5
            break
        cnt_5 -= 1

    if sum == 0:
        print(-1)
    else:
        print(sum)


main()

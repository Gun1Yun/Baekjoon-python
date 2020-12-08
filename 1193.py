"""
분수찾기
1 <= X <= 10^7 : int

==풀이==
1 > 2 > 3 > 4 > 5 로 증가하는 등차수열
지그재그 형태 => 홀, 짝 계산
"""
import sys
In = sys.stdin.readline


def main():
    x = int(In())
    denominator = 0

    while True:
        x -= denominator
        denominator += 1
        if x <= denominator:
            break

    if denominator % 2 == 0:
        numerator = x
        denominator = denominator - x + 1
    else:
        numerator = denominator - x + 1
        denominator = x

    print('%d/%d' % (numerator, denominator))


main()

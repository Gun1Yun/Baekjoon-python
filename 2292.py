"""
벌집
1 <= N <= 10^9  : int

== 풀이 ==
1 depth 당 6의 배수
1 6 12 18 24 30 ...
빼가면서 깊이 계산
"""
import sys
In = sys.stdin.readline


def main():
    n = int(In())
    cnt = 1
    n -= 1
    while n > 0:
        n -= cnt * 6
        cnt += 1

    print(cnt)


main()

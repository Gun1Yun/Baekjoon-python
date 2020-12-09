"""
ACM 호텔

==풀이==
1. 도착하는대로 빈방 배정
2. 손님 호텔 정문 가까운방 선호
3. W개 방, H층 건물 (1 <= H, W <= 99)
4. 인접한 방 거리 1
5. 거리가 같으면 아래층 선호
5. YYXX(층, 방)

y = n % h + 1
x = n // h + 1
"""
import sys
In = sys.stdin.readline


def solution(data):
    # data : [H, W, N] 층, 길이, 손님
    if data[2] % data[0] == 0:
        X = data[2] // data[0]
        Y = data[0]
    else:
        X = data[2] // data[0] + 1
        Y = data[2] % data[0]

    return Y, X


def main():
    data_cnt = int(In())
    data_set = []

    for _ in range(data_cnt):
        data = list(map(int, In().split()))
        data_set.append(data)

    for data in data_set:
        y, x = solution(data)
        if x < 10:
            print('%d0%d' % (y, x))
        else:
            print('%d%d' % (y, x))


main()

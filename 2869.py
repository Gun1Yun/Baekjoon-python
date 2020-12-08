"""
달팽이는 올라가고 싶다
1 <= B, A, V <= 10^9 : int

== 풀이 ==
막대 높이 : V
낮 : A
밤 : B
미리 전체에서 낮 빼주고 계산
"""
import sys
In = sys.stdin.readline


def main():
    day, night, height = map(int, In().split())
    velocity = day - night
    height -= day
    if height <= 0:
        date = 1
    else:
        if height % velocity == 0:
            date = 1 + height//velocity
        else:
            date = 1 + (height//velocity + 1)

    print(date)


main()

"""
터렛

==풀이==
조(x1, y1)
백(x2, y2)
조- r1
백- r2
두 원의 접점
"""
import sys
import math
In = sys.stdin.readline


def solving(data):
    sum_r = (data[2] + data[5])**2
    diff_r = (abs(data[2]-data[5]))**2

    distance = (data[0]-data[3])**2 + (data[1]-data[4])**2

    if distance == 0:
        if data[2] == data[5]:
            return -1
        else:
            return 0
    elif distance < sum_r and distance > diff_r:
        return 2
    elif distance == sum_r or diff_r == distance:
        return 1
    else:
        return 0


def main():
    case_cnt = int(In())
    dataset = []  # x1, y1, r1, x2, y2, r2
    for _ in range(case_cnt):
        dataset.append(list(map(int, In().split())))

    for data in dataset:
        print(solving(data))


main()

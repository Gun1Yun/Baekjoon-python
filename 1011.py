"""
Fly me to the Alpha Centauri

"""
import sys
import math
In = sys.stdin.readline


def solving(diff):
    n = math.ceil(math.sqrt(diff))
    if diff < n+(n-1)*(n-1):
        return 2*n-2
    else:
        return 2*n-1


def main():
    case_num = int(In())
    answers = []

    for _ in range(case_num):
        x, y = map(int, In().split())
        answers.append(solving(y-x))

    for answer in answers:
        print(answer)


main()

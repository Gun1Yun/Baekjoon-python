"""
부녀회장이 될테야

==풀이==
1. a층 b호 -> a-1층 1~b호까지 합 만큼
2. k층 n호 몇명
3. 0층부터 0층 i호는 i명

입력 : T(케이스 수), k, n(1 <= k, n <= 14)

재귀 이용하면 좋을것 같다.
k 층 부터 0층 까지
"""
import sys
In = sys.stdin.readline

"""
재귀함수 - 시간 초과
def solving(k, n):
    if k == 0:
        return n
    if n == 1:
        return 1

    return solving(k-1, n) + solving(k, n-1)
"""


def solving():
    # initial
    apt = [[0]*14 for _ in range(15)]
    for i in range(15):
        apt[i][0] = 1

    for i in range(14):
        apt[0][i] = i+1

    for i in range(14):
        for j in range(13):
            for k in range(j+2):
                apt[i+1][j+1] += apt[i][k]

    return apt


def main():
    case_cnt = int(In())
    case_set = []
    apt = solving()

    for _ in range(case_cnt):
        case = [int(In()), int(In())]
        case_set.append(case)

    for case in case_set:
        print(apt[case[0]][case[1]-1])


main()

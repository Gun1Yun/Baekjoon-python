"""
피보나치 함수

==풀이==
이전꺼 2개 합
"""
import sys
In = sys.stdin.readline


def solving():
    fib = [[0]*2 for _ in range(41)]
    fib[0][0] = 1
    fib[1][1] = 1

    for i in range(39):
        fib[i+2][0] = fib[i][0] + fib[i+1][0]
        fib[i+2][1] = fib[i][1] + fib[i+1][1]

    return fib


def main():
    case_cnt = int(In())
    dataset = []
    fib = solving()

    for _ in range(case_cnt):
        dataset.append(int(In()))

    for data in dataset:
        print('%d %d' % (fib[data][0], fib[data][1]))


main()

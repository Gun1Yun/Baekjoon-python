# 신입 사원
import sys
In = sys.stdin.readline


def recruit(scores):
    scores.sort(key=lambda x: x[0])
    cnt = 1

    if scores[0] == [1, 1]:
        return cnt

    best = scores[0][1]

    for doc in scores:
        if doc[1] == 1:
            cnt += 1
            break

        if doc[1] < best:
            best = doc[1]
            cnt += 1

    return cnt


def main():
    test_case = int(In())
    for _ in range(test_case):
        n = int(In())
        scores = []
        for i in range(n):
            scores.append(list(map(int, In().split())))
        print(recruit(scores))


if __name__ == "__main__":
    main()

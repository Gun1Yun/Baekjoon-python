# 신입 사원
import sys
In = sys.stdin.readline


def recruit(scores):
    documents = sorted(scores, key=lambda x: x[0])
    interviews = sorted(scores, key=lambda x: x[1])

    start = documents[0]
    finish = interviews[0]
    cnt = 1

    if start == finish:
        return cnt

    for doc in documents:
        if doc == finish:
            cnt += 1
            break
        if doc[1] < finish[0] and doc[1] < start[1]:
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

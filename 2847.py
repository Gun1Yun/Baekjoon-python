# 게임을 만든 동준이
import sys
In = sys.stdin.readline


def main():
    n = int(In())
    scores = []
    for _ in range(n):
        scores.append(int(In()))

    cnt = 0
    scores.reverse()

    for idx in range(len(scores)-1):
        if scores[idx] <= scores[idx+1]:
            while scores[idx] <= scores[idx+1]:
                scores[idx+1] -= 1
                cnt += 1

    print(cnt)


if __name__ == "__main__":
    main()

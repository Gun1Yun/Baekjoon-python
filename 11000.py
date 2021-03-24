# 강의실 배정
import sys
In = sys.stdin.readline


def main():
    n = int(In())
    classes = []
    for _ in range(n):
        classes.append(list(map(int, In().split())))

    classes = sorted(classes, key=lambda x: (x[1], x[0]))
    room = 1
    now = [classes[0][1]]

    for i in range(1, len(classes)):
        start, finish = classes[i]
        for j in range(len(now)):
            if now[j] <= start:
                now[j] = finish
                break

    print(cnt)


if __name__ == "__main__":
    main()

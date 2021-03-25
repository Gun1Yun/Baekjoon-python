# 강의실 배정
import sys
import heapq
In = sys.stdin.readline


def main():
    n = int(In())
    classes = []
    for _ in range(n):
        classes.append(list(map(int, In().split())))

    classes = sorted(classes, key=lambda x: (x[0], x[1]))
    rooms = []
    heapq.heappush(rooms, classes[0][1])

    for i in range(1, len(classes)):
        start, finish = classes[i]

        now = rooms[0]
        if now <= start:
            heapq.heappop(rooms)
            heapq.heappush(rooms, finish)
        else:
            heapq.heappush(rooms, finish)

    print(len(rooms))


if __name__ == "__main__":
    main()

import sys
In = sys.stdin.readline

# 1 <= n <= 100,000
# each w/k


def main():
    n = int(In())
    ropes = []
    for _ in range(n):
        ropes.append(int(In()))

    ropes.sort(reverse=True)

    answer = ropes[0]

    for cnt, rope in enumerate(ropes):
        if cnt == 0:
            continue
        weight = rope
        answer = max(answer, weight*(cnt+1))

    print(answer)


if __name__ == "__main__":
    main()

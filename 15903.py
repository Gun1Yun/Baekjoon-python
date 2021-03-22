# 카드 합체 놀이
import sys
In = sys.stdin.readline


def main():
    n, m = map(int, In().split())
    cards = list(map(int, In().split()))

    for _ in range(m):
        cards.sort()
        tmp = cards[0] + cards[1]
        cards[0] = tmp
        cards[1] = tmp

    print(sum(cards))


if __name__ == "__main__":
    main()
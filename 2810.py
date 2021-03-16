import sys
In = sys.stdin.readline


def main():
    line = int(In())
    seats = In().rstrip()

    cnt = 1
    couple = 0

    for seat in seats:
        if seat == 'S':
            cnt += 1

        if seat == 'L':
            if couple == 0:
                couple += 1
            else:
                couple = 0
                cnt += 1

    print(min(line, cnt))


if __name__ == "__main__":
    main()

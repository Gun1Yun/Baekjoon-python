# 전자레인지
import sys
In = sys.stdin.readline

# A B C
# 300초 60초 10초


def main():
    buttons = [300, 60, 10]
    time = int(In())

    answer = []

    for item in buttons:
        div = time // item
        time -= div*item
        answer.append(div)

    if time == 0:
        for i in answer:
            print(i, end=' ')
    else:
        print(-1)


if __name__ == "__main__":
    main()

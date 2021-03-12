# 캠핑
import sys
In = sys.stdin.readline


def main():
    cnt = 1
    while True:
        l, p, v = map(int, In().split())
        if l == 0:
            break
        div = v//p
        mod = min(v % p, l)
        answer = l*div + mod
        print('Case {}: {}'.format(
            cnt, answer
        ))
        cnt += 1


if __name__ == "__main__":
    main()

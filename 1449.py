# 수리공 항승
import sys
In = sys.stdin.readline


def main():
    n, l = map(int, In().split())
    leaks = list(map(int, In().split()))
    leaks.sort()

    tape = 0
    end_pos = 0

    for pos in leaks:
        if pos+0.5 <= end_pos:
            continue

        end_pos = pos + l - 0.5
        tape += 1

    print(tape)


if __name__ == "__main__":
    main()

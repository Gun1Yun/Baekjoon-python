import sys
In = sys.stdin.readline


def main():
    value = In().split('-')
    componet = [list(map(int, n.split('+'))) for n in value]
    result = sum(componet[0])
    for i in range(len(componet)-1):
        result -= sum(componet[i+1])
    print(result)


main()

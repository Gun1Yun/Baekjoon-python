# 단어 수학
import sys
from collections import defaultdict
In = sys.stdin.readline

expression = [[0]*8 for _ in range(10)]


def mapping(exp):
    dic = {}
    num = 9

    for i in range(8):
        tmp_dic = defaultdict(int)

        for j in range(10):
            c = exp[j][i]
            if c == 0 or c in dic.keys():
                continue
            tmp_dic[c] += 1

        rst = sorted(tmp_dic.items(), key=lambda item: item[1], reverse=True)
        for item in rst:
            dic[item[0]] = num
            num -= 1

    return calculate(exp, dic)


def calculate(exp, dic):
    answer = 0

    for i in range(8):
        k = 10**(7-i)
        for j in range(10):
            if exp[j][i] == 0:
                continue
            answer += dic[exp[j][i]]*k

    return answer


def main():
    n = int(In())
    words = []
    for _ in range(n):
        words.append(In().rstrip())

    words.sort(key=len, reverse=True)

    for i in range(n):
        word = words[i]
        idx = 1
        for j in range(7, 7-len(word), -1):
            expression[i][j] = word[len(word)-idx]
            idx += 1

    print(mapping(expression))


if __name__ == "__main__":
    main()

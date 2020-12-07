import sys
from itertools import combinations

"""
N : 회의 수
"""
i = 0
cnt = 0
N = int(sys.stdin.readline().rstrip())
time = []

while i < N:
    start, finish = map(int, sys.stdin.readline().rstrip().split())
    time.append([start, finish])
    i += 1

# 시간순 정렬
time = sorted(time)

for j in range(N):
    # 조합 계산
    combi_list = list(combinations(range(len(time)), j+1))
    for l in combi_list:
        check = True
        # 조합 여부 확인
        for k in range(len(l)-2):
            if time[l[k]][1] > time[l[k+1]][0]:
                check = False
                break
        if check:
            cnt = j+1
            break
    # check == False
    if not check:
        break

print(cnt)

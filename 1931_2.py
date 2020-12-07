import sys

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

for j in range(N-1):
    # t : start
    m = 1
    now = time[j][1]
    for t in range(j+1, N):
        nxt = time[t][0]
        if now > nxt:
            continue
        else:
            now = time[t][1]
            m += 1
    if m > cnt:
        cnt = m

print(cnt)

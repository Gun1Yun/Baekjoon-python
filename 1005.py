import sys
from collections import defaultdict, deque

In = sys.stdin.readline
order = defaultdict(list)


def bfs(target):
    visited = []
    queue = deque()
    queue.append(1)
    visited.append(1)

    while queue:


def main():
    t = int(In())   # Test case

    for _ in range(t):
        '''
        n : number of buildings
        k : number of rules
        '''
        n, k = map(int, In().split())
        cost = list(map(int, In().split()))
        for _ in range(k):
            # rules
            b1, b2 = map(int, In().split())
            order[b1].append(b2)
            order[b2].append(b1)
        w = int(In())   # building num


if __name__ == "__main__":
    main()

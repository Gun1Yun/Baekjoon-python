import sys
from collections import defaultdict, deque

sys.setrecursionlimit(10**6)
In = sys.stdin.readline


def dfs(order, start, cost, building_cost):

    for b in order[start]:
        building_cost[b] = max(
            building_cost[b], building_cost[start] + cost[b-1])
        dfs(order, b, cost, building_cost)


def main():
    t = int(In())   # Test case

    for _ in range(t):
        '''
        n : number of buildings
        k : number of rules
        '''
        n, k = map(int, In().split())
        cost = list(map(int, In().split()))
        order = defaultdict(list)

        for _ in range(k):
            # rules
            b1, b2 = map(int, In().split())
            order[b2].append(b1)
        w = int(In())   # building num

        building_cost = defaultdict(int)
        building_cost[w] = cost[w-1]

        dfs(order, w, cost, building_cost)

        print(max(building_cost.values()))


if __name__ == "__main__":
    main()

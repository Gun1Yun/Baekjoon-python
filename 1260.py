import sys
from collections import defaultdict

In = sys.stdin.readline
visited = []

def bfs(graph, v_start):
    


def dfs(graph, v_start):
    visited.append(v_start)

    for vertex in graph[v_start]:
        if vertex not in visited:
            dfs(graph, vertex)


def main():
    v_num, e_num, v_start = map(int, In().split())
    graph = defaultdict(list)
    for _ in range(e_num):
        v1, v2 = map(int, In().split())
        graph[v1].append(v2)
        graph[v2].append(v1)

    for key in graph:
        graph[key].sort()

    dfs(graph, v_start)

    print(visited)


main()

import sys
from itertools import count

input = sys.stdin.readline
# 입력 처리
N = int(input().strip())
M = int(input().strip())

graph = [[False] * (N+1) for _ in range(N+1)]
visited = [False] * (N + 1)


def dfs(node):
    global graph, visited
    visited[node] = True
    for next in range(1, N+1):
        if not visited[next] and graph[node][next]:
            dfs(next)

for _ in range(M):
    a, b = map(int, input().split())
    graph[a][b] = True
    graph[b][a] = True

dfs(1)
print(visited.count(True) - 1)
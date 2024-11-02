import sys

input = sys.stdin.readline

# 입력
n, m = map(int, input().split())

# 그래프
graph = [[] for _ in range(n)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)


# dfs 검색
def dfs(node, depth, visited):
    if depth == 4:
        return True

    visited[node] = True
    for neighbor in graph[node]:
        if not visited[neighbor]:
            if dfs(neighbor, depth + 1, visited):
                return True
    visited[node] = False
    return False


found = False
for i in range(n):
    visited = [False] * n
    if dfs(i, 0, visited):
        print(1)
        found = True
        break

if not found:
    print(0)

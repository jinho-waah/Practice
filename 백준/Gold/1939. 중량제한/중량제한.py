import sys
from collections import defaultdict

input = sys.stdin.readline

# 입력 처리
N, M = map(int, input().split())
graph = defaultdict(dict)

for _ in range(M):
    A, B, C = map(int, input().split())

    if B in graph[A]:
        if C > graph[A][B]:
            graph[A][B] = C
            graph[B][A] = C
    else:
        graph[A][B] = C
        graph[B][A] = C

first, second = map(int, input().split())

def bfs(start, end, weight):
    queue = [start]
    visited = [False] * (N + 1)
    visited[start] = True

    while queue:
        current = queue.pop()

        if current == end:
            return True

        for neighbor, limit in graph[current].items():
            if not visited[neighbor] and limit >= weight:
                visited[neighbor] = True
                queue.append(neighbor)

    return False

low, high = 1, 1000000000
answer = low
while low <= high:
    mid = (low + high) // 2

    if bfs(first, second, mid):
        answer = mid
        low = mid + 1
    else:
        high = mid - 1

print(answer)

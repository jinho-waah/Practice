import sys
from collections import defaultdict, deque
from statistics import mean
from itertools import combinations
input = sys.stdin.readline
import math
sys.setrecursionlimit(2000)


# 입력 처리
N, M = map(int, input().split())  # 학생 수 N, 비교 횟수 M

# 학생 간 키 비교 정보를 저장할 그래프 (작은 -> 큰)
graph = [[] for _ in range(N + 1)]
reverse_graph = [[] for _ in range(N + 1)]

# 그래프 초기화
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    reverse_graph[b].append(a)

# BFS 함수 정의
def bfs(start, graph):
    queue = deque([start])
    visited = [False] * (N + 1)
    visited[start] = True
    count = 0

    while queue:
        current = queue.popleft()
        for neighbor in graph[current]:
            if not visited[neighbor]:
                visited[neighbor] = True
                queue.append(neighbor)
                count += 1

    return count

# 자신의 키가 몇 번째인지 알 수 있는 학생 수 계산
result = 0
for i in range(1, N + 1):
    greater_count = bfs(i, graph)  # 자신보다 큰 학생 수
    smaller_count = bfs(i, reverse_graph)  # 자신보다 작은 학생 수
    if greater_count + smaller_count == N - 1:
        result += 1

# 결과 출력
print(result)
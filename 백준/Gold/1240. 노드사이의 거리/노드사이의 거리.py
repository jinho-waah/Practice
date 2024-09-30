import sys
from collections import defaultdict, deque

input = sys.stdin.readline
sys.setrecursionlimit(2000)

# 입력 처리
N, M = map(int, input().split())  # 노드의 개수 N과 쿼리 개수 M

# 트리 구성
tree = defaultdict(list)
for _ in range(N - 1):
    u, v, w = map(int, input().split())
    tree[u].append((v, w))
    tree[v].append((u, w))

# 두 노드 사이의 거리를 구하는 함수
def bfs(start, end):
    # BFS를 사용해 두 노드 사이의 최단 거리 구함.
    queue = deque([(start, 0)])
    visited = [False] * (N + 1)
    visited[start] = True

    while queue:
        current, dist = queue.popleft()
        if current == end:
            return dist

        for neighbor, weight in tree[current]:
            if not visited[neighbor]:
                visited[neighbor] = True
                queue.append((neighbor, dist + weight))

# 쿼리 입력 및 처리
queries = [tuple(map(int, input().split())) for _ in range(M)]

# 각 쿼리에 대해 거리 계산
for u, v in queries:
    print(bfs(u, v))

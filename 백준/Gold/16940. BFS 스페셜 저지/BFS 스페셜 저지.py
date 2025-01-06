import sys
input = sys.stdin.readline
from collections import defaultdict, deque

def build_graph(edges):
    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)
    return graph

def is_valid_bfs(graph, bfs_order):
    n = len(bfs_order)
    visited = [False] * (n + 1)
    index = 0

    order_index = {node: i for i, node in enumerate(bfs_order)}

    queue = deque([1])
    visited[1] = True

    while queue:
        current = queue.popleft()

        if bfs_order[index] != current:
            return 0
        index += 1

        neighbors = []
        for neighbor in graph[current]:
            if not visited[neighbor]:
                neighbors.append(neighbor)
                visited[neighbor] = True

        neighbors.sort(key=lambda x: order_index[x])
        queue.extend(neighbors)

    return 1 if index == n else 0


N = int(input())
edges = [tuple(map(int, input().split())) for _ in range(N-1)]
bfs_order = list(map(int, input().split()))

# 그래프 생성
graph = build_graph(edges)

# 결과 출력
print(is_valid_bfs(graph, bfs_order))

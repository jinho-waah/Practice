from collections import defaultdict, deque
import sys
input = sys.stdin.readline

def find_farthest_node(start, graph, n):
    """DFS를 사용하여 start 노드에서 가장 먼 노드와 그 거리를 반환"""
    visited = [-1] * (n + 1)
    visited[start] = 0
    stack = deque([start])
    farthest_node = start
    max_distance = 0

    while stack:
        current = stack.popleft()

        for neighbor, weight in graph[current]:
            if visited[neighbor] == -1:  # 방문하지 않은 경우
                visited[neighbor] = visited[current] + weight
                stack.append(neighbor)

                # 현재까지 가장 먼 노드 갱신
                if visited[neighbor] > max_distance:
                    max_distance = visited[neighbor]
                    farthest_node = neighbor

    return farthest_node, max_distance

def tree_diameter(n, edges):
    """트리의 지름 계산"""
    # 그래프 생성 (인접 리스트)
    graph = defaultdict(list)
    for u, v, w in edges:
        graph[u].append((v, w))
        graph[v].append((u, w))

    # 첫 번째 DFS: 임의의 노드(1번 노드)에서 가장 먼 노드 찾기
    farthest_node, _ = find_farthest_node(1, graph, n)

    # 두 번째 DFS: 첫 번째 DFS에서 찾은 노드에서 가장 먼 노드 찾기
    _, diameter = find_farthest_node(farthest_node, graph, n)

    return diameter

n = int(input().strip())
edges = []

for _ in range(n-1):
    u, v, w = map(int, input().split())
    edges.append((u,v,w))

print(tree_diameter(n, edges))
import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

def dijkstra(start, graph, n):
    distance = [INF] * (n + 1)
    distance[start] = 0
    pq = []
    heapq.heappush(pq, (0, start))

    while pq:
        dist, node = heapq.heappop(pq)
        if dist > distance[node]:
            continue

        for next_node, weight in graph[node]:
            cost = dist + weight
            if cost < distance[next_node]:
                distance[next_node] = cost
                heapq.heappush(pq, (cost, next_node))

    return distance

def solve(n, m, x, edges):
    # 그래프 초기화
    graph = [[] for _ in range(n + 1)]
    reverse_graph = [[] for _ in range(n + 1)]

    # 간선 입력
    for u, v, t in edges:
        graph[u].append((v, t))
        reverse_graph[v].append((u, t))  # 역방향 그래프

    # 각 마을에서 X로 가는 최단 거리 계산
    distance_to_x = dijkstra(x, reverse_graph, n)

    # X에서 각 마을로 돌아오는 최단 거리 계산
    distance_from_x = dijkstra(x, graph, n)

    # 왕복 거리 계산
    max_time = 0
    for i in range(1, n + 1):
        max_time = max(max_time, distance_to_x[i] + distance_from_x[i])

    return max_time

# 입력 처리
n, m, x = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(m)]

# 결과 출력
print(solve(n, m, x, edges))

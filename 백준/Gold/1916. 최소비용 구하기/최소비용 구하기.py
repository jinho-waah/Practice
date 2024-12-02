import sys
input = sys.stdin.readline

INF = int(1e9)

import heapq
def dijkstra(n, start, end, graph):
    # 거리 테이블 초기화
    distance = [INF] * (n + 1)
    distance[start] = 0

    # 우선순위 큐
    pq = []
    heapq.heappush(pq, (0, start))  # (비용, 현재 정점)

    while pq:
        cost, current = heapq.heappop(pq)

        # 이미 처리된 정점은 무시
        if distance[current] < cost:
            continue

        # 인접 정점 확인
        for next_node, weight in graph[current]:
            next_cost = cost + weight

            # 더 짧은 경로 발견 시 업데이트
            if next_cost < distance[next_node]:
                distance[next_node] = next_cost
                heapq.heappush(pq, (next_cost, next_node))

    return distance[end]

# 입력 처리
N = int(input())  # 도시의 개수
M = int(input())  # 버스의 개수

# 그래프 초기화
graph = [[] for _ in range(N + 1)]

for _ in range(M):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))

# 출발점과 도착점
start, end = map(int, input().split())

# 최소 비용 계산 및 출력
print(dijkstra(N, start, end, graph))
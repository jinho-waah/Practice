import sys
from collections import defaultdict, deque
from statistics import mean
import heapq
from itertools import combinations
input = sys.stdin.readline
import math
sys.setrecursionlimit(2000)


INF = float('inf')
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def dijkstra(n, cave):
    # 최소 비용 테이블 초기화
    min_cost = [[INF] * n for _ in range(n)]
    min_cost[0][0] = cave[0][0]
    # 우선순위 큐를 사용한 다익스트라 알고리즘 적용
    pq = [(cave[0][0], 0, 0)]  # (비용, 행, 열)
    heapq.heapify(pq)

    while pq:
        cost, x, y = heapq.heappop(pq)

        # 현재 위치에서 상하좌우 이동
        for dx, dy in directions:
            nx, ny = x + dx, y + dy

            if 0 <= nx < n and 0 <= ny < n:
                new_cost = cost + cave[nx][ny]

                # 더 적은 비용으로 해당 칸에 도달할 수 있다면 갱신
                if new_cost < min_cost[nx][ny]:
                    min_cost[nx][ny] = new_cost
                    heapq.heappush(pq, (new_cost, nx, ny))

    return min_cost[n-1][n-1]

problem_number = 1
while True:
    # 입력 처리
    n = int(input().strip())
    if n == 0:
        break

    cave = [list(map(int, input().split())) for _ in range(n)]
    # 최소 비용 계산
    result = dijkstra(n, cave)
    # 결과 출력
    print(f"Problem {problem_number}: {result}")
    problem_number += 1
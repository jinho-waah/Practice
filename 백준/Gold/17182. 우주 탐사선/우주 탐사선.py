import sys
from collections import defaultdict, deque
from statistics import mean
import heapq
from itertools import combinations
input = sys.stdin.readline
import math
sys.setrecursionlimit(2000)


# 입력 처리
N, K = map(int, input().split())
dist = [list(map(int, input().split())) for _ in range(N)]
INF = float('inf')

# 플로이드-워셜 알고리즘으로 모든 정점 간 최단 거리 계산
for k in range(N):
    for i in range(N):
        for j in range(N):
            if dist[i][j] > dist[i][k] + dist[k][j]:
                dist[i][j] = dist[i][k] + dist[k][j]

# DP와 비트마스킹을 이용한 모든 행성 방문하기
# dp[visited][current] : 현재 current에 있고, visited 상태일 때의 최소 비용
dp = [[INF] * N for _ in range(1 << N)]
dp[1 << K][K] = 0  # 시작 위치에서 출발, 시작 행성 방문 처리

# 모든 상태를 순회
for visited in range(1 << N):
    for current in range(N):
        if visited & (1 << current):
            for next_node in range(N):
                if not (visited & (1 << next_node)):  # 아직 방문하지 않은 노드
                    next_visited = visited | (1 << next_node)
                    dp[next_visited][next_node] = min(dp[next_visited][next_node], dp[visited][current] + dist[current][next_node])

# 모든 행성을 방문한 상태에서 최소 비용 찾기
final_state = (1 << N) - 1
min_cost = min(dp[final_state][i] for i in range(N))

print(min_cost)
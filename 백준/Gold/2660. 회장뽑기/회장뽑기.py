import sys
from collections import defaultdict, deque
from statistics import mean
from itertools import combinations
input = sys.stdin.readline
import math
sys.setrecursionlimit(2000)


# 입력 처리
N = int(input().strip())  # 회원 수
friend_relation = []

# 친구 관계 입력
while True:
    a, b = map(int, input().split())
    if a == -1 and b == -1:
        break
    friend_relation.append((a, b))

# 그래프 초기화 (플로이드-워셜을 위한 초기값 설정)
INF = float('inf')
graph = [[INF] * (N + 1) for _ in range(N + 1)]

# 자기 자신으로 가는 거리는 0으로 초기화
for i in range(1, N + 1):
    graph[i][i] = 0

# 친구 관계 입력 반영 (무방향 그래프)
for a, b in friend_relation:
    graph[a][b] = 1
    graph[b][a] = 1


# 플로이드-워셜 알고리즘을 사용하여 모든 쌍 최단 거리 계산
for k in range(1, N + 1):
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            if graph[i][j] > graph[i][k] + graph[k][j]:
                graph[i][j] = graph[i][k] + graph[k][j]

# 각 회원의 점수 계산 (최대 거리)
scores = [0] * (N + 1)
for i in range(1, N + 1):
    scores[i] = max(graph[i][1:])  # i 회원의 점수는 i에서 다른 회원까지의 최단 거리 중 최대값

# 회장 후보 선정
min_score = min(scores[1:])  # 최소 점수 찾기
candidates = [i for i in range(1, N + 1) if scores[i] == min_score]

# 출력
print(min_score, len(candidates))
print(" ".join(map(str, candidates)))
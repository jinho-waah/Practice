import sys
from collections import defaultdict, deque
from statistics import mean
import heapq
from itertools import combinations

input = sys.stdin.readline
import math
sys.setrecursionlimit(2000)


# 입력 처리
# n 지역의 개수, m 수색 범위, r 길의 개수
n, m, r = map(int, input().split())
# 각 구역의 아이템 개수
t = list(map(int, input().split()))
loc = set()
for _ in range(r):
    # l은 a,b 지역의 거리
    a, b, l = map(int,input().split())
    loc.add((a, b, l))

INF = float('inf')
dist = [[INF] * n for _ in range(n)]

for i in range(n):
    dist[i][i] = 0

for a,b,l in loc:
    a -= 1
    b -= 1
    dist[a][b] = l
    dist[b][a] = l

for k in range(n):
    for i in range(n):
        for j in range(n):
            dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

max_items = 0

for i in range(n):
    total_items = 0
    for j in range(n):
        if dist[i][j] <= m:
            total_items += t[j]
    max_items = max(max_items, total_items)

# 결과 출력
print(max_items)
import sys
from collections import defaultdict, deque
from statistics import mean
import heapq
from itertools import combinations
import math
sys.setrecursionlimit(2000)

input = sys.stdin.readline


N, M = map(int, input().split())

candy = [[0] * (M + 1)]

for _ in range(N):
    row = [0] + list(map(int, input().split()))
    candy.append(row)


dp = [[0] * (M + 1) for _ in range(N + 1)]

for i in range(1, N + 1):
    for j in range(1, M + 1):
        dp[i][j] = max(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + candy[i][j]


print(dp[N][M])
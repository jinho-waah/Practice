import sys
from collections import defaultdict, deque
from statistics import mean
from itertools import combinations
input = sys.stdin.readline
sys.setrecursionlimit(2000)

# 입력 처리
N = int(input())
children = list(int(input()) for _ in range(N))

# DP를 이용한 최장 증가 부분 수열 (LIS) 길이 구하기
dp = [1] * N

for i in range(1, N):
    for j in range(i):
        if children[j] < children[i]:
            dp[i] = max(dp[i], dp[j] + 1)
            # [1, 1, 1, 1, 1, 1, 1]
            # [1, 2, 1, 1, 1, 1, 1]
            # [1, 2, 2, 1, 1, 1, 1]
            # [1, 2, 2, 1, 2, 1, 1]
            # [1, 2, 2, 1, 3, 1, 1]
            # [1, 2, 2, 1, 3, 1, 1]
            # [1, 2, 2, 1, 3, 1, 2]
            # [1, 2, 2, 1, 3, 1, 2]

# 최장 증가 부분 수열의 길이
lis_length = max(dp)

# 최소로 옮겨야 하는 아이들의 수
result = N - lis_length
print(result)
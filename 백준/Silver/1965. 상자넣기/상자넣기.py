import sys
from collections import defaultdict, deque
from statistics import mean
from itertools import combinations
input = sys.stdin.readline
sys.setrecursionlimit(2000)

# 입력 처리
n = int(input())
box_list = list(map(int,input().split()))
# 증가하는 부분 수열(Longest Increasing Subsequence, LIS)이용
# DP 배열 생성
dp = [1] * n  # 모든 원소가 최소한 자기 자신으로 LIS 길이 1을 가짐

# LIS 계산
for i in range(n):
    for j in range(i):
        if box_list[j] < box_list[i]:
            dp[i] = max(dp[i], dp[j] + 1)

# 최댓값 출력
print(max(dp))
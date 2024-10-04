import sys
from collections import defaultdict, deque
from statistics import mean
from itertools import combinations
input = sys.stdin.readline
sys.setrecursionlimit(2000)

# 입력 처리
N = int(input())
A = list(map(int, input().split()))

# 증가하는 부분 수열 (LIS) 계산
dp_inc = [1] * N
for i in range(1, N):
    for j in range(i):
        if A[j] < A[i]:
            dp_inc[i] = max(dp_inc[i], dp_inc[j] + 1)
# 감소하는 부분 수열 (LDS) 계산
dp_dec = [1] * N
for i in range(N-2, -1, -1):
    for j in range(i+1, N):
        if A[j] < A[i]:
            dp_dec[i] = max(dp_dec[i], dp_dec[j] + 1)
# 바이토닉 부분 수열의 최대 길이 계산
max_length = 0
for i in range(N):
    max_length = max(max_length, dp_inc[i] + dp_dec[i] - 1)

print(max_length)
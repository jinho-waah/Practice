import sys
from collections import defaultdict, deque
from statistics import mean
import heapq
from itertools import combinations

input = sys.stdin.readline
import math
sys.setrecursionlimit(2000)


# 입력 처리
data = []
while True:
    latest_data = int(input().strip())
    if latest_data == 0:
        break
    data.append(latest_data)

# 최대값까지의 소수를 구하기 위한 에라토스테네스의 체
MAX = 1000000
is_prime = [True] * (MAX + 1)
is_prime[0] = is_prime[1] = False

for i in range(2, int(MAX ** 0.5) + 1):
    if is_prime[i]:
        for j in range(i * i, MAX + 1, i):
            is_prime[j] = False

# 각 테스트 케이스에 대해 처리
for n in data:
    found = False
    # a는 홀수 소수로, b = n - a가 소수인지 확인
    for a in range(3, n // 2 + 1, 2):
        if is_prime[a] and is_prime[n - a]:
            print(f"{n} = {a} + {n - a}")
            found = True
            break
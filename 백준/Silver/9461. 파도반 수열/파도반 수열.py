import sys
from collections import defaultdict, deque
from statistics import mean
from itertools import combinations
input = sys.stdin.readline
sys.setrecursionlimit(2000)

# 입력 처리
T = int(input())
N_list = [int(input()) for i in range(T)]

padovan_dict = defaultdict(int)
padovan_dict[1] = 1
padovan_dict[2] = 1
padovan_dict[3] = 1

for N in N_list:
    for i in range(3,N+1):
        padovan_dict[i] = padovan_dict[i-2] + padovan_dict[i-3]
    print(padovan_dict[N])

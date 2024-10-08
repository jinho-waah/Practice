import sys
from collections import defaultdict, deque
from statistics import mean
import heapq
from itertools import combinations
input = sys.stdin.readline
import math
sys.setrecursionlimit(2000)


# 입력 처리
first_string = input().strip()
second_string = input().strip()

count = 0
index = 0
second_len = len(second_string)

while index <= len(first_string) - second_len:
    if first_string[index:index + second_len] == second_string:
        count += 1
        index += second_len
    else:
        index += 1

print(count)
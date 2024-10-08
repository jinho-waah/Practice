import sys
from collections import defaultdict, deque
from statistics import mean
import heapq
from itertools import combinations
input = sys.stdin.readline
import math
sys.setrecursionlimit(2000)


# 입력 처리
bingo = []
mc = []
for _ in range(5):
    bingo.append(list(map(int, input().split())))

for _ in range(5):
    mc.extend(list(map(int, input().split())))

position = {}
for i in range(5):
    for j in range(5):
        position[bingo[i][j]] = (i, j)

marked = [[False] * 5 for _ in range(5)]


def check_bingo():
    bingo_count = 0

    # 가로 체크
    for i in range(5):
        if all(marked[i]):
            bingo_count += 1

    # 세로 체크
    for i in range(5):
        if all(marked[j][i] for j in range(5)):
            bingo_count += 1

    # 대각선 체크 (왼쪽 위에서 오른쪽 아래로)
    if all(marked[i][i] for i in range(5)):
        bingo_count += 1

    # 대각선 체크 (오른쪽 위에서 왼쪽 아래로)
    if all(marked[i][4 - i] for i in range(5)):
        bingo_count += 1

    return bingo_count >= 3

for turn, num in enumerate(mc):
    if num in position:
        r, c = position[num]
        marked[r][c] = True


    if check_bingo():
        print(turn + 1)
        break
import sys
from collections import defaultdict, deque
from statistics import mean
from itertools import combinations
input = sys.stdin.readline
import math
sys.setrecursionlimit(2000)


# 입력 처리
N = int(input().strip())
K = int(input().strip())
sensors = list(map(int, input().split()))

# 센서가 1개이거나, 집중국이 센서보다 많을 경우
if K >= N:
    print(0)
else:
    # 센서들을 정렬
    sensors.sort()

    # 인접한 센서 간의 거리 계산
    distances = []
    for i in range(1, N):
        distances.append(sensors[i] - sensors[i - 1])

    # 거리를 내림차순으로 정렬하여 가장 큰 K-1개의 거리를 잘라냄
    distances.sort(reverse=True)

    # 전체 거리 합에서 K-1개의 큰 거리를 빼줌
    result = sum(distances[K-1:])
    print(result)
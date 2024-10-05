import sys
from collections import defaultdict, deque
import heapq
from statistics import mean
from itertools import combinations
input = sys.stdin.readline
import math
sys.setrecursionlimit(2000)


# 입력 처리
N = int(input().strip())
weights = list(map(int, input().split()))

# 저울추들을 오름차순 정렬
weights.sort()

# 초기 target은 1로 설정 (1부터 측정할 수 있는지 체크)
target = 1

for weight in weights:
    # 만약 현재 추를 추가했을 때 target을 넘어버리면 더 이상 그 무게를 만들 수 없음
    if weight > target:
        break
    # target까지의 무게를 만들 수 있으면, target + weight까지도 가능해짐
    target += weight

# 측정할 수 없는 최소 무게 출력
print(target)
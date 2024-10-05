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
lectures = []

for _ in range(N):
    _, start, end = map(int, input().split())
    lectures.append((start, end))

# 시작 시간 기준으로 오름차순 정렬
lectures.sort()

# 우선순위 큐 사용: 종료 시간을 기준으로 최소 힙 생성
heap = []

# 첫 번째 강의의 종료 시간을 힙에 추가
heapq.heappush(heap, lectures[0][1])

# 나머지 강의 처리
for i in range(1, N):
    start, end = lectures[i]

    # 현재 강의의 시작 시간이 가장 먼저 끝나는 강의실의 종료 시간 이후인 경우
    if heap[0] <= start:
        heapq.heappop(heap)  # 해당 강의실을 재사용할 수 있으므로 종료 시간 제거

    # 현재 강의의 종료 시간을 힙에 추가 (새로운 강의실 배정 또는 기존 갱신)
    heapq.heappush(heap, end)

# 힙에 남아 있는 종료 시간의 개수가 필요한 강의실의 수
print(len(heap))
import heapq
import sys
from collections import defaultdict
input = sys.stdin.readline

N = int(input())

# 두 개의 힙 선언
# stack 이든 뭐든 중간 값을 구하라 하면
# 두개의 배열을 이용하면 편함
max_heap = []  # 최대 힙 (중간값 이하를 저장)
min_heap = []  # 최소 힙 (중간값 이상을 저장)

for _ in range(N):
    num = int(input())

    # 먼저 최대 힙에 넣음
    if len(max_heap) == len(min_heap):
        heapq.heappush(max_heap, -num)
    else:
        heapq.heappush(min_heap, num)

    # 최대 힙의 루트가 최소 힙의 루트보다 크다면 교환해야 함
    if min_heap and -max_heap[0] > min_heap[0]:
        max_val = -heapq.heappop(max_heap)
        min_val = heapq.heappop(min_heap)
        heapq.heappush(max_heap, -min_val)
        heapq.heappush(min_heap, max_val)

    # 현재까지 중간값은 최대 힙의 루트
    print(-max_heap[0])
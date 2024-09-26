import heapq
import sys

input = sys.stdin.readline

# 입력 처리
N =int(input())
heap = []
for _ in range(N):
    x = int(input())

    if x != 0:
        heapq.heappush(heap, x)
    else:
        if heap:
            print(heapq.heappop(heap))
        else:
            print(0)
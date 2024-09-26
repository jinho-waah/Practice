import heapq
import sys
from collections import defaultdict
input = sys.stdin.readline

N = int(input())
# 이 문제를 풀때는 간단하게 적은 수의 합을 구하면 됨
heap = []
for _ in range(N):
    heapq.heappush(heap, int(input()))

result = 0

# 카드 묶음이 2개 이상일 때까지 합침
while len(heap) > 1:
    # 가장 작은 두 묶음을 꺼내서 합친다
    first = heapq.heappop(heap)
    second = heapq.heappop(heap)
    current_sum = first + second
    result += current_sum  # 비교 횟수 추가

    # 합친 묶음을 다시 힙에 넣는다
    heapq.heappush(heap, current_sum)

print(result)
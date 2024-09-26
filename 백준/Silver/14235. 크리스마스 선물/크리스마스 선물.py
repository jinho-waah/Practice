import heapq
import sys

input = sys.stdin.readline

# 입력 처리
n = int(input())
heap = []

for _ in range(n):
    a = list(map(int, input().split()))

    if a[0] == 0:
        # heap이 비어 있으면 0을 출력
        if heap:
            print(-heapq.heappop(heap))
        else:
            print(-1)
    else:
        # 입력값이 0이 아니면 주어진 수들을 힙에 추가
        for i in range(1, len(a)):
            heapq.heappush(heap, -a[i])  # 최대 힙을 만들기 위해 음수로 저장

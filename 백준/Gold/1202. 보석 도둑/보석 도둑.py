import heapq
import sys

input = sys.stdin.readline

# 입력 처리
N, K = map(int, input().split())
jewels = []
bags = []

# 보석 정보 입력
for _ in range(N):
    M, V = map(int, input().split())
    jewels.append((M, V))

# 가방 정보 입력
for _ in range(K):
    C = int(input())
    bags.append(C)

# 보석을 무게 기준으로 정렬
jewels.sort()
# 가방을 무게 기준으로 정렬
bags.sort()

max_value = 0
heap = []
jewel_idx = 0

# 각 가방에 대해 가능한 보석을 선택
for bag in bags:
    # 현재 가방에 담을 수 있는 보석들을 힙에 추가
    while jewel_idx < N and jewels[jewel_idx][0] <= bag:
        heapq.heappush(heap, -jewels[jewel_idx][1])  # 최대 힙으로 사용하기 위해 음수로 저장
        jewel_idx += 1

    # 가장 가치가 높은 보석을 선택
    if heap:
        max_value += -heapq.heappop(heap)

# 결과 출력
print(max_value)

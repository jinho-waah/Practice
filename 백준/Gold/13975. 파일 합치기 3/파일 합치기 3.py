import sys
import heapq

input = sys.stdin.readline

# 테스트 케이스 수 입력
T = int(input().strip())

for _ in range(T):
    K = int(input().strip())
    chapter_list = list(map(int, input().split()))
    heapq.heapify(chapter_list)

    total_cost = 0

    while len(chapter_list) != 1:
        first = heapq.heappop(chapter_list)
        second =  heapq.heappop(chapter_list)
        cost = first + second
        total_cost += cost

        heapq.heappush(chapter_list, cost)

    print(total_cost)
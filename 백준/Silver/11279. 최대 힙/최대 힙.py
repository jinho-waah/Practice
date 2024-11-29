import heapq
import sys

input = sys.stdin.readline

def solve():
    n = int(input())
    max_heap = []

    result = []
    for _ in range(n):
        x = int(input())
        if x > 0:
            # 힙에 음수로 삽입
            heapq.heappush(max_heap, -x)
        elif x == 0:
            # 힙에서 최대값 꺼내기
            if max_heap:
                result.append(-heapq.heappop(max_heap))
            else:
                result.append(0)

    # 결과 출력
    print("\n".join(map(str, result)))

# 실행
solve()

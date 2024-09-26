import heapq
import sys

input = sys.stdin.readline

# 입력 처리
N, H, T = map(int, input().split())
giants = [-int(input()) for _ in range(N)]
heapq.heapify(giants)

# 뿅망치를 사용한 횟수
hammer_count = 0
for i in range(T):
    if -giants[0] == 1 or -giants[0] < H:
        break
    else:
        heapq.heapreplace(giants, -(-giants[0] // 2))
        hammer_count += 1


if -giants[0] < H:
    print("YES")
    print(hammer_count)
else:
    print("NO")
    print(-giants[0])
# while hammer_count < T:
#     # 가장 큰 거인을 꺼냄
#     tallest = -heapq.heappop(giants)
#
#     # 만약 가장 큰 거인이 센티보다 작다면 종료
#     if tallest < H:
#         heapq.heappush(giants, -tallest)
#         break
#
#     # 키가 1인 경우 더 줄어들 수 없으므로 break
#     if tallest == 1:
#         heapq.heappush(giants, -tallest)
#         break
#
#     # 뿅망치를 사용해서 키를 절반으로 줄임
#     new_height = tallest // 2
#     heapq.heappush(giants, -new_height)
#     hammer_count += 1
#
# # 결과 확인
# tallest_remaining = -heapq.heappop(giants)
# if tallest_remaining < H:
#     print("YES")
#     print(hammer_count)
# else:
#     print("NO")
#     print(tallest_remaining)

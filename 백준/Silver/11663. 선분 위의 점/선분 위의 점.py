import sys
from itertools import count
from collections import deque
from bisect import bisect_left, bisect_right

input = sys.stdin.readline
# 입력 처리
N, M = map(int, input().split())  # 점의 개수 N과 선분의 개수 M
points = list(map(int, input().split()))  # 점의 좌표
line = [tuple(map(int, input().split())) for _ in range(M)]  # 선분의 시작점과 끝점

points.sort()
results = []
for start, end in line:
    # start 이상인 첫 위치와 end 이하인 마지막 위치를 찾음
    left_index = bisect_left(points, start)
    right_index = bisect_right(points, end)

    # 개수 계산
    count = right_index - left_index
    results.append(count)

# 결과 출력

for i in results:
    print(i)
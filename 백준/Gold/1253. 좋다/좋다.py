import sys
from bisect import bisect_left

input = sys.stdin.readline

# 입력 처리
N = int(input().strip())
number_list = list(map(int, input().split()))
number_list.sort()  # 리스트를 정렬

count = 0

# 각 원소에 대해 탐색
for k in range(N):
    target = number_list[k]  # 현재 타겟이 되는 수
    left, right = 0, N - 1

    while left < right:
        if left == k:
            left += 1
            continue
        if right == k:
            right -= 1
            continue

        current_sum = number_list[left] + number_list[right]

        if current_sum == target:
            count += 1
            break  # 하나만 찾으면 되므로 종료
        elif current_sum < target:
            left += 1
        else:
            right -= 1

print(count)

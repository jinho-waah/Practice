import heapq
import sys

input = sys.stdin.readline

# 입력 처리
N = int(input())
number_list = list(map(int, input().split()))
S = int(input())


for i in range(N):
    # 현재 위치 i부터 S만큼의 범위 내에서 가장 큰 값을 찾음
    max_idx = i
    for j in range(i + 1, min(i + 1 + S, N)):
        if number_list[j] > number_list[max_idx]:
            max_idx = j

    # 현재 위치의 원소와 가장 큰 값의 위치가 다르다면 교환
    if max_idx != i:
        # max_idx의 원소를 앞으로 가져오기 위해 교환
        for j in range(max_idx, i, -1):
            number_list[j], number_list[j - 1] = number_list[j - 1], number_list[j]
            S -= 1  # 교환했으므로 S를 감소

        # 교환 가능 횟수가 0이 되면 더 이상 정렬을 진행할 수 없음
        if S <= 0:
            break

# 결과 출력
print(" ".join(map(str, number_list)))
import heapq
# 확통 수학 문제
# 알몸이 아닌경우 == 하나라도 걸친 경우
# 알몸인 경우는 단 한가지이므로 계산하기 편함
# (item1 + 1) * (item2 + 1) * (item3 + 1) .... - 1
# item에 1을 더한 이유는 걸치지 않았을 경우를 위해
# -1 을 한 이유는 모든 경우의 수에서 알몸인 경우를 빼기 위해
import sys
from collections import defaultdict
input = sys.stdin.readline

T = int(input())  # 목표 합
n = int(input())  # 배열 A의 크기
A = list(map(int, input().split()))  # 배열 A
m = int(input())  # 배열 B의 크기
B = list(map(int, input().split()))  # 배열 B

# A 배열 합을 저장할 딕셔너리
sum_A = defaultdict(int)
sum_B = defaultdict(int)

# sum_A에 대한 부분 배열 합 전체 표현
for i in range(n):
    total = 0
    for j in range(i, n):
        total += A[j]
        sum_A[total] += 1

# sum_B에 대한 부분 배열 합 전체 표현
for i in range(m):
    total = 0
    for j in range(i, m):
        total += B[j]
        sum_B[total] += 1

result = 0

for dict_item in sum_A:
    if (T - dict_item) in sum_B:
        # 경우의 수 계산 후 결과값에 더하기
        result += sum_A[dict_item] * sum_B[T-dict_item]

print(result)
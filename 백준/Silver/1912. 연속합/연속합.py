import sys

input = sys.stdin.readline

# 입력 받기
N = int(input().strip())
A = list(map(int, input().split()))

max_sum = A[0]  # 초기 최대값은 첫 번째 원소
current_sum = A[0]

for i in range(1, N):
    # 현재 위치에서의 최대 부분합 갱신
    current_sum = max(A[i], current_sum + A[i])
    max_sum = max(max_sum, current_sum)

# 결과 출력
print(max_sum)

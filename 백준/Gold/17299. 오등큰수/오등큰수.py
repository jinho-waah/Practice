import sys
from collections import defaultdict

input = sys.stdin.readline

# 입력 받기
N = int(input().strip())
A = list(map(int, input().split()))

# 각 원소의 등장 횟수를 세기 위한 딕셔너리
count = defaultdict(int)
for num in A:
    count[num] += 1

# 오등큰수 결과를 저장할 배열
result = [-1] * N

# 인덱스를 저장할 스택
stack = []

# 오른쪽에서 오등큰수를 탐색
for i in range(N):
    # 스택이 비어있지 않고, 현재 원소의 등장 횟수가 스택의 top에 있는 원소의 등장 횟수보다 클 경우
    while stack and count[A[stack[-1]]] < count[A[i]]:
        result[stack.pop()] = A[i]
    # 현재 인덱스를 스택에 추가
    stack.append(i)

# 결과 출력
print(" ".join(map(str, result)))
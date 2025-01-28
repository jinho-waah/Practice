import sys
input = sys.stdin.readline

def can_transform_recursive(S, T):
    # 기본 종료 조건: T의 길이가 S와 같아진 경우
    if len(T) == len(S):
        return 1 if S == T else 0

    # 마지막 문자가 'A'인 경우
    if T[-1] == 'A':
        if can_transform_recursive(S, T[:-1]):
            return 1

    # 첫 번째 문자가 'B'인 경우
    if T[0] == 'B':
        if can_transform_recursive(S, T[1:][::-1]):
            return 1

    # 변환 불가능한 경우
    return 0

# 입력 처리
S = input().strip()
T = input().strip()

# 결과 출력
print(can_transform_recursive(S, T))
import sys
from collections import defaultdict, deque
input = sys.stdin.readline
sys.setrecursionlimit(2000)

# 회문 검사 함수
def is_palindrome(s, left, right):
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True

# 입력 처리
T = int(input().strip())
string_list = [input().strip() for _ in range(T)]

for word in string_list:
    left, right = 0, len(word) - 1

    # 기본 회문 검사
    while left < right:
        if word[left] == word[right]:
            left += 1
            right -= 1
        else:
            # 유사회문 검사: 왼쪽 또는 오른쪽을 무시한 경우 중 하나가 회문인지 확인
            if is_palindrome(word, left + 1, right) or is_palindrome(word, left, right - 1):
                print(1)  # 유사회문
            else:
                print(2)  # 회문도, 유사회문도 아님
            break
    else:
        # 회문인 경우
        print(0)
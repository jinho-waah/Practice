import sys
input = sys.stdin.readline

def min_insertions_to_palindrome(sequence):
    n = len(sequence)
    reverse_sequence = sequence[::-1]

    # DP 배열 초기화 (1차원 배열 사용)
    prev = [0] * (n + 1)
    curr = [0] * (n + 1)

    # LCS 계산
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if sequence[i - 1] == reverse_sequence[j - 1]:
                curr[j] = prev[j - 1] + 1
            else:
                curr[j] = max(prev[j], curr[j - 1])
        prev, curr = curr, prev

    # LPS 길이
    lps_length = prev[n]

    # 최소 삽입 개수 계산
    return n - lps_length

# 입력 처리
n = int(input().strip())
sequence = list(map(int, input().strip().split()))

# 결과 출력
print(min_insertions_to_palindrome(sequence))


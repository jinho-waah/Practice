import sys
from collections import defaultdict, deque
input = sys.stdin.readline
sys.setrecursionlimit(2000)

# 입력 처리
# N = input().strip()

word1 = input().strip()
word2 = input().strip()
word3 = input().strip()

len1, len2, len3 = len(word1), len(word2), len(word3)

# 3차원 배열 생성
lcs = [[[0] * (len3 + 1) for _ in range(len2 + 1)] for _ in range(len1 + 1)]
# lcs 계산
for i in range(1, len1 + 1):
    for j in range(1, len2 + 1):
        for k in range(1, len3 + 1):
            if word1[i - 1] == word2[j - 1] == word3[k - 1]:
                lcs[i][j][k] = lcs[i - 1][j - 1][k - 1] + 1
            else:
                lcs[i][j][k] = max(lcs[i - 1][j][k], lcs[i][j - 1][k], lcs[i][j][k - 1])

# 결과 출력
print(lcs[len1][len2][len3])

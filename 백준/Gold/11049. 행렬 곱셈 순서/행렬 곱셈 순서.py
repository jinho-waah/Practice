import sys
input = sys.stdin.readline

# 입력
N = int(input().strip())
matrices = [tuple(map(int, input().split())) for _ in range(N)]
# DP 테이블 초기화
dp = [[0] * N for _ in range(N)]

# DP 수행
for length in range(1, N):  # length는 행렬 곱의 길이
    for i in range(N - length):
        j = i + length
        dp[i][j] = float('inf')
        for k in range(i, j):
            # dp[i][j]의 최솟값 갱신
            dp[i][j] = min(dp[i][j], dp[i][k] + dp[k+1][j]  + matrices[i][0] * matrices[k][1] * matrices[j][1])

# 결과 출력
print(dp[0][N-1])


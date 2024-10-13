N, K = map(int, input().split())

# DP 테이블 초기화
MOD = 1000000000
dp = [[0] * (N + 1) for _ in range(K + 1)]

# dp[i][0]은 1로 초기화 (모든 i에 대해 0을 만드는 방법은 한 가지)
for i in range(K + 1):
    dp[i][0] = 1

# 점화식을 이용해 DP 테이블 채우기
for i in range(1, K + 1):
    for j in range(1, N + 1):
        dp[i][j] = (dp[i-1][j] + dp[i][j-1]) % MOD

# 결과 출력
print(dp[K][N])

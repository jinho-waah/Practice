import sys
input = sys.stdin.readline

def binomial_coefficient(n, k):
    MOD = 10007

    # DP 테이블 초기화
    dp = [[0] * (k + 1) for _ in range(n + 1)]

    # 점화식에 따라 DP 계산
    for i in range(n + 1):
        for j in range(min(i, k) + 1):
            if j == 0 or j == i:  # \(\binom{N}{0} = \binom{N}{N} = 1\)
                dp[i][j] = 1
            else:
                dp[i][j] = (dp[i - 1][j - 1] + dp[i - 1][j]) % MOD

    return dp[n][k]

# 입력 처리
n, k = map(int, input().split())

# 결과 출력
print(binomial_coefficient(n, k))

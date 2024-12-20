import sys
input = sys.stdin.readline

def tile_ways(n):
    if n % 2 == 1:
        return 0  # 홀수는 불가능
    dp = [0] * (n + 1)
    dp[0] = 1
    dp[2] = 3

    for i in range(4, n + 1, 2):
        dp[i] = dp[i - 2] * 3
        for j in range(4, i + 1, 2):
            dp[i] += dp[i - j] * 2

    return dp[n]

# 입력 처리
N = int(input().strip())
print(tile_ways(N))

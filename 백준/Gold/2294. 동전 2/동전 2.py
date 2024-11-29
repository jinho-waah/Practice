import sys
input = sys.stdin.readline

def min_coins(n, k, coins):
    # DP 배열 초기화
    dp = [float('inf')] * (k + 1)
    dp[0] = 0  # 0원을 만들기 위해 필요한 동전 개수는 0

    # 동전 사용하여 DP 갱신
    for coin in coins:
        for i in range(coin, k + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)

    # 결과 반환
    return dp[k] if dp[k] != float('inf') else -1

# 입력 처리
n, k = map(int, input().split())
coins = [int(input()) for _ in range(n)]

# 결과 출력
print(min_coins(n, k, coins))
import sys
input = sys.stdin.readline

def count_valid_equations(n, numbers):
    # DP 테이블 초기화: dp[i][j]는 i번째 숫자까지 계산했을 때 값 j가 나오는 경우의 수
    dp = [[0] * 21 for _ in range(n)]
    dp[0][numbers[0]] = 1  # 첫 번째 숫자는 그대로 사용

    # DP 계산
    for i in range(1, n - 1):  # 마지막 숫자는 결과로 사용하므로 제외
        for j in range(21):  # 가능한 값은 0~20
            if dp[i - 1][j] > 0:  # 이전 단계에서 유효한 값만 고려
                if j + numbers[i] <= 20:  # 덧셈
                    dp[i][j + numbers[i]] += dp[i - 1][j]
                if j - numbers[i] >= 0:  # 뺄셈
                    dp[i][j - numbers[i]] += dp[i - 1][j]

    # 마지막 숫자를 결과로 사용
    return dp[n - 2][numbers[-1]]

# 입력 처리
n = int(input().strip())
numbers = list(map(int, input().strip().split()))

# 결과 계산 및 출력
print(count_valid_equations(n, numbers))

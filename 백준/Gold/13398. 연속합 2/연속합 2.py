import sys
input = sys.stdin.readline

def max_subarray_with_one_removal(n, arr):
    # dp 배열 초기화
    dp = [0] * n  # 원소를 제거하지 않은 경우
    dp_del = [0] * n  # 원소를 제거한 경우

    dp[0] = arr[0]
    dp_del[0] = arr[0]
    result = arr[0]

    for i in range(1, n):
        dp[i] = max(dp[i - 1] + arr[i], arr[i])  # 기존 수열을 연속하거나 새로운 시작
        dp_del[i] = max(dp_del[i - 1] + arr[i], dp[i - 1])  # 하나를 제거하거나 포함
        result = max(result, dp[i], dp_del[i])  # 결과 갱신

    return result


# 입력 처리
n = int(input().strip())
arr = list(map(int, input().split()))

# 결과 출력
print(max_subarray_with_one_removal(n, arr))

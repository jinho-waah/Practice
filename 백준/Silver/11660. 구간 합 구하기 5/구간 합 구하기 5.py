import sys
input = sys.stdin.readline

# 입력 처리
N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

# DP 배열 초기화
prefix_sum = [[0] * (N + 1) for _ in range(N + 1)]

# DP 배열 채우기 (누적 합)
for i in range(1, N + 1):
    for j in range(1, N + 1):
        prefix_sum[i][j] = (
            prefix_sum[i - 1][j] +  # 상단
            prefix_sum[i][j - 1] -  # 좌측
            prefix_sum[i - 1][j - 1] +  # 중복 제거
            arr[i - 1][j - 1]  # 현재 값
        )

# 쿼리 처리
results = []
for _ in range(M):
    x1, y1, x2, y2 = map(int, input().split())

    # 구간 합 계산
    total = (
        prefix_sum[x2][y2]
        - (prefix_sum[x1 - 1][y2] if x1 > 1 else 0)
        - (prefix_sum[x2][y1 - 1] if y1 > 1 else 0)
        + (prefix_sum[x1 - 1][y1 - 1] if x1 > 1 and y1 > 1 else 0)
    )
    results.append(total)

# 결과 출력
for i in results:
    print(i)

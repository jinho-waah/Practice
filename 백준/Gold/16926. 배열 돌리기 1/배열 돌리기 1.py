import sys
input = sys.stdin.readline

def rotate_matrix(n, m, r, matrix):
    layers = min(n, m) // 2  # 층의 개수

    for layer in range(layers):
        # 현재 층의 범위
        top, bottom = layer, n - layer - 1
        left, right = layer, m - layer - 1

        # 현재 층의 원소 추출
        elements = []
        for i in range(left, right + 1):  # 위쪽
            elements.append(matrix[top][i])
        for i in range(top + 1, bottom + 1):  # 오른쪽
            elements.append(matrix[i][right])
        for i in range(right - 1, left - 1, -1):  # 아래쪽
            elements.append(matrix[bottom][i])
        for i in range(bottom - 1, top, -1):  # 왼쪽
            elements.append(matrix[i][left])

        # 회전
        length = len(elements)
        r_mod = r % length
        rotated = elements[r_mod:] + elements[:r_mod]

        # 회전된 원소를 다시 넣기
        idx = 0
        for i in range(left, right + 1):  # 위쪽
            matrix[top][i] = rotated[idx]
            idx += 1
        for i in range(top + 1, bottom + 1):  # 오른쪽
            matrix[i][right] = rotated[idx]
            idx += 1
        for i in range(right - 1, left - 1, -1):  # 아래쪽
            matrix[bottom][i] = rotated[idx]
            idx += 1
        for i in range(bottom - 1, top, -1):  # 왼쪽
            matrix[i][left] = rotated[idx]
            idx += 1

    return matrix

# 입력 처리
N, M, R = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(N)]

# 결과 계산
rotated_matrix = rotate_matrix(N, M, R, matrix)

# 결과 출력
for row in rotated_matrix:
    print(*row)

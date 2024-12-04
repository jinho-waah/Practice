from collections import deque

# 특정 방향에서 직사각형이 유효한지 검사
def is_valid(grid, n, m, h, w, r, c, direction):
    # 격자판을 벗어나는 경우
    if r < 0 or c < 0 or r + h > n or c + w > m:
        return False

    # 이동 방향에 따른 경계 검사
    if direction == "up":
        for col in range(c, c + w):
            if grid[r][col] == 1:
                return False
    elif direction == "down":
        for col in range(c, c + w):
            if grid[r + h - 1][col] == 1:
                return False
    elif direction == "left":
        for row in range(r, r + h):
            if grid[row][c] == 1:
                return False
    elif direction == "right":
        for row in range(r, r + h):
            if grid[row][c + w - 1] == 1:
                return False

    return True

def bfs(grid, n, m, h, w, sr, sc, fr, fc):
    directions = [(-1, 0, "up"), (1, 0, "down"), (0, -1, "left"), (0, 1, "right")]
    visited = [[False] * m for _ in range(n)]
    queue = deque([(sr, sc, 0)])  # (행, 열, 이동 횟수)
    visited[sr][sc] = True

    while queue:
        r, c, dist = queue.popleft()

        # 도착점에 도달한 경우
        if (r, c) == (fr, fc):
            return dist

        # 다음 이동 탐색
        for dr, dc, direction in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < n and 0 <= nc < m and not visited[nr][nc]:
                if is_valid(grid, n, m, h, w, nr, nc, direction):
                    visited[nr][nc] = True
                    queue.append((nr, nc, dist + 1))

    return -1  # 도달할 수 없는 경우

# 입력 처리
import sys
input = sys.stdin.readline

n, m = map(int, input().split())  # 격자판 크기
grid = [list(map(int, input().split())) for _ in range(n)]
h, w, sr, sc, fr, fc = map(int, input().split())

# 1-based index를 0-based index로 변환
sr, sc, fr, fc = sr - 1, sc - 1, fr - 1, fc - 1

# BFS 수행 및 결과 출력
print(bfs(grid, n, m, h, w, sr, sc, fr, fc))

import sys
from collections import deque
input = sys.stdin.readline

# BFS 함수 정의
def bfs(grid, visited, x, y, color, is_colorblind):
    n = len(grid)
    queue = deque([(x, y)])
    visited[x][y] = True

    while queue:
        cx, cy = queue.popleft()
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:  # 상하좌우 탐색
            nx, ny = cx + dx, cy + dy
            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
                # 적록색약인 경우: R과 G를 같은 색으로 처리
                if is_colorblind:
                    if grid[nx][ny] in "RG" and color in "RG":
                        visited[nx][ny] = True
                        queue.append((nx, ny))
                    if grid[nx][ny] == color:
                        visited[nx][ny] = True
                        queue.append((nx, ny))
                else:  # 일반 경우
                    if grid[nx][ny] == color:
                        visited[nx][ny] = True
                        queue.append((nx, ny))

# 적록색약이 아닌 경우와 적록색약인 경우 구역 계산 함수
def count_regions(grid, is_colorblind):
    n = len(grid)
    visited = [[False] * n for _ in range(n)]
    regions = 0

    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                bfs(grid, visited, i, j, grid[i][j], is_colorblind)
                regions += 1
    return regions

# 입력 처리
N = int(input().strip())
screen = [input().strip() for _ in range(N)]

# 결과 계산
normal_count = count_regions(screen, is_colorblind=False)  # 적록색약이 아닌 경우
colorblind_count = count_regions(screen, is_colorblind=True)  # 적록색약인 경우

# 결과 출력
print(normal_count, colorblind_count)

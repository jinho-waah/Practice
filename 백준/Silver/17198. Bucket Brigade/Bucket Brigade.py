import sys
from itertools import count
from collections import deque

input = sys.stdin.readline
# 입력 처리
N = 10
farm = [input().strip() for _ in range(N)]

visited = [[False] * N for _ in range(N)]

barn = None
lake = None
rock = None

# 기본 dfs
def bfs(start, end):
    queue = deque([(start[0], start[1], 0)])  # (row, col, distance)
    visited[start[0]][start[1]] = True

    while queue:
        r, c, dist = queue.popleft()

        # 만약 end 지점에 도달하면 거리 반환
        if (r, c) == end:
            return dist - 1  # 헛간이나 호수 바로 앞칸까지만 필요하므로 -1

        # 인접한 네 방향으로 탐색
        for dr, dc in directions:
            nr, nc = r + dr, c + dc

            if not 0 <= nr < N or not 0 <= nc < N: continue

            if not visited[nr][nc] and farm[nr][nc] != 'R':
                visited[nr][nc] = True
                queue.append((nr, nc, dist + 1))

# graph 값 채우기
for i in range(N):
    for j in range(N):
        if farm[i][j] == 'B':
            barn = (i, j)
        elif farm[i][j] == 'L':
            lake = (i, j)
        elif farm[i][j] == 'R':
            rock = (i, j)

directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

# 최소 거리 계산
min_distance = bfs(lake, barn)
print(min_distance)
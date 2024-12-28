from collections import deque
import sys
input = sys.stdin.readline

def min_walls_to_break(m, n, maze):
    # 방향 벡터 (상, 하, 좌, 우)
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    dist = [[float('inf')] * m for _ in range(n)]
    dist[0][0] = 0

    # 0-1 BFS를 위한 덱
    queue = deque([(0, 0)])

    while queue:
        x, y = queue.popleft()

        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < m:
                cost = dist[x][y] + maze[nx][ny]
                if cost < dist[nx][ny]:
                    dist[nx][ny] = cost
                    if maze[nx][ny] == 0:
                        queue.appendleft((nx, ny))  # 빈 방이면 앞에 추가
                    else:
                        queue.append((nx, ny))  # 벽이면 뒤에 추가

    return dist[n-1][m-1]

# 입력 처리
m, n = map(int, input().split())
maze = [list(map(int, input().strip())) for _ in range(n)]

# 결과 출력
print(min_walls_to_break(m, n, maze))

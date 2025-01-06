import sys
from collections import deque

def bfs(space, shark_size, start, n):
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    queue = deque([(start[0], start[1], 0)])  # (x, y, distance)
    visited = [[False] * n for _ in range(n)]
    visited[start[0]][start[1]] = True

    fish = []
    while queue:
        x, y, dist = queue.popleft()

        for dx, dy in directions:
            nx, ny = x + dx, y + dy

            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
                if space[nx][ny] <= shark_size:  # Can move
                    visited[nx][ny] = True
                    queue.append((nx, ny, dist + 1))

                    if 0 < space[nx][ny] < shark_size:  # Can eat
                        fish.append((dist + 1, nx, ny))

    if fish:
        fish.sort()  # Sort by distance, then row, then column
        return fish[0]  # Closest fish
    return None

def solve():
    input = sys.stdin.readline
    n = int(input().strip())
    space = [list(map(int, input().split())) for _ in range(n)]

    # Find initial position of the shark
    for i in range(n):
        for j in range(n):
            if space[i][j] == 9:
                shark_pos = (i, j)
                space[i][j] = 0  # Clear the shark's initial position

    shark_size = 2
    time = 0
    eaten = 0

    while True:
        result = bfs(space, shark_size, shark_pos, n)
        if result is None:  # No more fish to eat
            break

        dist, nx, ny = result
        time += dist
        eaten += 1

        # Move shark
        shark_pos = (nx, ny)
        space[nx][ny] = 0

        # Increase shark size
        if eaten == shark_size:
            shark_size += 1
            eaten = 0

    print(time)

# 실행
solve()

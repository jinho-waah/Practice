import sys
from collections import defaultdict, deque
from statistics import mean
import heapq
from itertools import combinations
import math
sys.setrecursionlimit(2000)

input = sys.stdin.readline


N, M = map(int, input().split())
map_data = [list(map(int, input().strip())) for _ in range(N)]  # 지도 정보


def bfs(N, M, map_data):
    # 상, 하, 좌, 우 방향 이동 설정
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    visited = [[[0] * M for _ in range(N)] for _ in range(2)]

    queue = deque([(0, 0, 0)])
    visited[0][0][0] = 1

    while queue:
        x, y, broken = queue.popleft()

        if x == N - 1 and y == M - 1:
            return visited[broken][x][y]

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]


            if 0 <= nx < N and 0 <= ny < M:
                # 벽을 만나지 않았을 경우 (0인 경우)
                if map_data[nx][ny] == 0 and visited[broken][nx][ny] == 0:
                    visited[broken][nx][ny] = visited[broken][x][y] + 1
                    queue.append((nx, ny, broken))

                if map_data[nx][ny] == 1 and broken == 0 and visited[1][nx][ny] == 0:
                    visited[1][nx][ny] = visited[broken][x][y] + 1
                    queue.append((nx, ny, 1))

    return -1


print(bfs(N, M, map_data))


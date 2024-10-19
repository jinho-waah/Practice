import sys

input = sys.stdin.readline


N, M = map(int,input().split())

dot = [list(input().strip()) for _ in range(N)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

visited = [[False] * M for _ in range(N)]



def dfs(x, y, start_x, start_y, color, count):
    visited[x][y] = True

    for direction in range(4):
        nx = x + dx[direction]
        ny = y + dy[direction]

        if 0 <= nx < N and 0 <= ny < M:

            if dot[nx][ny] == color:
                if not visited[nx][ny]:
                    if dfs(nx, ny, start_x, start_y, color, count + 1):
                        return True
                elif nx == start_x and ny == start_y and count >= 4:
                    return True

    visited[x][y] = False
    return False


def has_cycle():
    for i in range(N):
        for j in range(M):
            if not visited[i][j]:
                if dfs(i, j, i, j, dot[i][j], 1):
                    return True
    return False


# 결과 출력
if has_cycle():
    print("Yes")
else:
    print("No")

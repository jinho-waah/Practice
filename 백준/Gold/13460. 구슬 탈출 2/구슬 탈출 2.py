import sys
from collections import deque

input = sys.stdin.readline

def move(x, y, dx, dy, board):
    count = 0
    while board[x + dx][y + dy] != '#' and board[x][y] != 'O':
        x += dx
        y += dy
        count += 1
    return x, y, count

def solve(board, n, m):
    for i in range(n):
        for j in range(m):
            if board[i][j] == 'R':
                rx, ry = i, j
            elif board[i][j] == 'B':
                bx, by = i, j

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    queue = deque([(rx, ry, bx, by, 0)])
    visited = set((rx, ry, bx, by))

    while queue:
        rx, ry, bx, by, depth = queue.popleft()

        if depth >= 10:
            return -1

        for dx, dy in directions:
            nrx, nry, r_count = move(rx, ry, dx, dy, board)
            nbx, nby, b_count = move(bx, by, dx, dy, board)

            if board[nbx][nby] == 'O':
                continue

            if board[nrx][nry] == 'O':
                return depth + 1

            if (nrx, nry) == (nbx, nby):
                if r_count > b_count:
                    nrx -= dx
                    nry -= dy
                else:
                    nbx -= dx
                    nby -= dy

            if (nrx, nry, nbx, nby) not in visited:
                visited.add((nrx, nry, nbx, nby))
                queue.append((nrx, nry, nbx, nby, depth + 1))

    return -1


M, N = map(int, input().split())
maze = list(input().strip() for _ in range(M))

print(solve(maze, M, N))
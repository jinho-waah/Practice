import sys
from collections import deque

input = sys.stdin.readline

def is_within_bounds(x, y, N, M):
    return 0 <= x < N and 0 <= y < M

def earth_quake(grid, start):
    global count
    tmp_for_after_shake = deque()
    col = len(grid)
    row = len(grid[0])

    # 가로줄 양의 방향 =======================================================
    for k in range(1, 3):
        new_x = start[0] + k
        if is_within_bounds(new_x, start[1], col, row):
            if grid[new_x][start[1]][0] == "|":
                break
            elif grid[new_x][start[1]][1] == 1:
                tmp_for_after_shake.append((new_x, start[1]))
                grid[new_x][start[1]][1] = 0
                count += 1
            elif grid[new_x][start[1]][1] == 2:
                grid[new_x][start[1]][1] = 1

    # 가로줄 음의 방향 =======================================================
    for k in range(1, 3):
        new_x = start[0] - k
        if is_within_bounds(new_x, start[1], col, row):
            if grid[new_x][start[1]][0] == "|":
                break
            elif grid[new_x][start[1]][1] == 1:
                tmp_for_after_shake.append((new_x, start[1]))
                grid[new_x][start[1]][1] = 0
                count += 1
            elif grid[new_x][start[1]][1] == 2:
                grid[new_x][start[1]][1] = 1

    # 세로줄 양의 방향 =======================================================
    for l in range(1, 3):
        new_y = start[1] + l
        if is_within_bounds(start[0], new_y, col, row):
            if grid[start[0]][new_y][0] == "|":
                break
            elif grid[start[0]][new_y][1] == 1:
                tmp_for_after_shake.append((start[0], new_y))
                grid[start[0]][new_y][1] = 0
                count += 1
            elif grid[start[0]][new_y][1] == 2:
                grid[start[0]][new_y][1] = 1

    # 세로줄 음의 방향 =======================================================
    for l in range(1, 3):
        new_y = start[1] - l
        if is_within_bounds(start[0], new_y, col, row):
            if grid[start[0]][new_y][0] == "|":
                break
            elif grid[start[0]][new_y][1] == 1:
                tmp_for_after_shake.append((start[0], new_y))
                grid[start[0]][new_y][1] = 0
                count += 1
            elif grid[start[0]][new_y][1] == 2:
                grid[start[0]][new_y][1] = 1

    # 여진 처리 (재귀 대신 반복문으로 처리)
    after_shake(grid, tmp_for_after_shake)

def after_shake(grid, points):
    global count
    col = len(grid)
    row = len(grid[0])

    # BFS 방식으로 여진 처리
    while points:
        p, q = points.popleft()

        # 아래쪽 확인
        if is_within_bounds(p + 1, q, col, row):
            if grid[p + 1][q][1] == 1:
                grid[p + 1][q][1] = 0
                points.append((p + 1, q))
                count += 1
            elif grid[p + 1][q][1] == 2:
                grid[p + 1][q][1] = 1
        # 위쪽 확인
        if is_within_bounds(p - 1, q, col, row):
            if grid[p - 1][q][1] == 1:
                grid[p - 1][q][1] = 0
                points.append((p - 1, q))
                count += 1
            elif grid[p - 1][q][1] == 2:
                grid[p - 1][q][1] = 1

        # 오른쪽 확인
        if is_within_bounds(p, q + 1, col, row):
            if grid[p][q + 1][1] == 1:
                grid[p][q + 1][1] = 0
                points.append((p, q + 1))
                count += 1
            elif grid[p][q + 1][1] == 2:
                grid[p][q + 1][1] = 1

        # 왼쪽 확인
        if is_within_bounds(p, q - 1, col, row):
            if grid[p][q - 1][1] == 1:
                grid[p][q - 1][1] = 0
                points.append((p, q - 1))
                count += 1
            elif grid[p][q - 1][1] == 2:
                grid[p][q - 1][1] = 1

# 입력 받기
N, M = map(int, input().split())
grid = []
start_ = []
count = 0

for i in range(N):
    row_ = input().strip()
    manipulate_list = []
    for j in range(len(row_)):
        if row_[j] == "@":
            manipulate_list.append([row_[j], "o"])
            start_ = [i, j]
        elif row_[j] == ".":
            manipulate_list.append([row_[j], "o"])
        elif row_[j] == "*":
            manipulate_list.append([row_[j], 1])
        elif row_[j] == "#":
            manipulate_list.append([row_[j], 2])
        elif row_[j] == "|":
            manipulate_list.append([row_[j], "x"])

    grid.append(manipulate_list)

# 지진 시작
earth_quake(grid, start_)

# 결과 계산 및 출력
tmp = 0
for line in grid:
    for ele in line:
        if isinstance(ele[1], int):
            if ele[1] > 0:
                tmp += 1

print(count, tmp)

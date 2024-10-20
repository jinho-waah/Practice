import sys

input = sys.stdin.readline


N, M, x, y, K = map(int, input().split())
map_data = [list(map(int, input().split())) for _ in range(N)]
commands = list(map(int, input().split()))

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

dice = [0] * 7 # 0, 윗면, 북, 동, 서, 남, 바닥면 (0은 계산하기 편하려고 넣은 순서

def roll_dice(direction):
    if direction == 1:  # 동쪽으로 굴림
        dice[3], dice[6], dice[1], dice[4] \
            = dice[1], dice[3], dice[4], dice[6]
    elif direction == 2:  # 서쪽으로 굴림
        dice[4], dice[1], dice[6], dice[3] \
            = dice[1], dice[3], dice[4], dice[6]
    elif direction == 3:  # 북쪽으로 굴림
        dice[2], dice[6], dice[1], dice[5] \
            = dice[1], dice[2], dice[5], dice[6]
    elif direction == 4:  # 남쪽으로 굴림
        dice[5], dice[1], dice[6], dice[2] \
            = dice[1], dice[2], dice[5], dice[6]

for c in commands:
    map_x = x + dx[c - 1]
    map_y = y + dy[c - 1]

    if 0 <= map_x < N and 0 <= map_y < M:
        roll_dice(c)

        if map_data[map_x][map_y] == 0:
            map_data[map_x][map_y] = dice[6]

        else:
            dice[6] = map_data[map_x][map_y]
            map_data[map_x][map_y] = 0

        print(dice[1])

        # 좌표 갱신
        x, y = map_x, map_y
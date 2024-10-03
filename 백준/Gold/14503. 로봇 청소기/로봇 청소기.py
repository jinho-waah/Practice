import sys
from collections import defaultdict, deque
from statistics import mean
input = sys.stdin.readline
sys.setrecursionlimit(2000)

# 입력 처리
N, M = map(int, input().split())
coord_x, coord_y, dir = map(int, input().split())
room = [list(map(int, input().split())) for _ in range(N)]

# 북(0), 동(1), 남(2), 서(3)
directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

# 현재 칸을 청소한 칸 수
cleaned_count = 0

while True:
    # 1. 현재 칸 청소
    if room[coord_x][coord_y] == 0:
        room[coord_x][coord_y] = -1  # 청소 완료 표시
        cleaned_count += 1

    # 2. 왼쪽 방향으로 회전 및 이동 가능한지 확인
    found_new_place = False
    for _ in range(4):
        # 왼쪽 방향으로 회전
        dir = (dir - 1) % 4
        next_x, next_y = coord_x + directions[dir][0], coord_y + directions[dir][1]

        # 그 방향에 청소하지 않은 공간이 있는 경우 한 칸 전진
        if 0 <= next_x < N and 0 <= next_y < M and room[next_x][next_y] == 0:
            coord_x, coord_y = next_x, next_y
            found_new_place = True
            break

    # 3. 네 방향 모두 청소가 이미 되어있거나 벽인 경우
    if not found_new_place:
        # 바라보는 방향 유지하고 후진
        back_dir = (dir + 2) % 4
        back_x, back_y = coord_x + directions[back_dir][0], coord_y + directions[back_dir][1]

        # 뒤쪽이 벽이라 후진 불가능하면 작동 종료
        if room[back_x][back_y] == 1:
            break
        else:
            # 후진 가능하면 위치 이동
            coord_x, coord_y = back_x, back_y

# 결과 출력
print(cleaned_count)
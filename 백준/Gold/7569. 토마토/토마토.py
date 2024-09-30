import sys
from collections import defaultdict, deque
input = sys.stdin.readline
sys.setrecursionlimit(2000)

# 입력 처리
M, N, H = map(int, input().split())

boxes = []

for h in range(H):
    box = []
    for n in range(N):
        row = list(map(int, input().split()))
        box.append(row)
    boxes.append(box)

# boxes는 H x N x M 크기의 3차원 배열로, 각 토마토의 상태를 담고 있습니다.
# boxes[h][n][m] 형태로 접근할 수 있습니다.

# z 양의 방향, y 양의 방향, x 양의 방향
# z 음의 방향, y 음의 방향, x 음의 방향
directions = [(1, 0, 0), (0, 1, 0), (0, 0, 1), (-1, 0, 0), (0, -1, 0), (0, 0, -1)]

queue = deque()
for z in range(H):
    for y in range(N):
        for x in range(M):
            if boxes[z][y][x] == 1:
                queue.append((z, y, x))  # 익은 토마토의 좌표를 큐에 추가

# BFS 탐색 시작
while queue:
    z, y, x = queue.popleft()

    for dz, dy, dx in directions:
        nz, ny, nx = z + dz, y + dy, x + dx
        # 범위 내에 있고 익지 않은 토마토인 경우
        if 0 <= nz < H and 0 <= ny < N and 0 <= nx < M and boxes[nz][ny][nx] == 0:
            boxes[nz][ny][nx] = boxes[z][y][x] + 1  # 현재 일수 + 1로 갱신
            queue.append((nz, ny, nx))
# 최소 일수 계산
max_days = 0
all_ripe = True  # 모든 토마토가 익었는지 여부를 체크하는 플래그

for z in range(H):
    for y in range(N):
        for x in range(M):
            if boxes[z][y][x] == 0:
                # 익지 않은 토마토가 있다면 -1을 출력
                all_ripe = False
            max_days = max(max_days, boxes[z][y][x])

# 결과 출력
if all_ripe:
    # 처음 시작이 1이었기 때문에, 최종 일수는 -1 해줍니다.
    print(max_days - 1)
else:
    print(-1)
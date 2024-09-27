import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)
# 입력 처리
R, C = map(int, input().split())
grid = [list(input().strip()) for _ in range(R)]
# 이동 방향 (상, 하, 좌, 우)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 방문 여부 체크
visited = [[False] * C for _ in range(R)]


# DFS 함수 정의
def dfs(x, y):
    global sheep, wolves
    visited[x][y] = True

    # 현재 위치가 양일 경우
    if grid[x][y] == 'k':
        sheep += 1
    # 현재 위치가 늑대일 경우
    elif grid[x][y] == 'v':
        wolves += 1

    # 상, 하, 좌, 우로 탐색
    for i in range(4):
        dx_, dy_ = x + dx[i], y + dy[i]
        if 0 <= dx_ < R and 0 <= dy_ < C and not visited[dx_][dy_] and grid[dx_][dy_] != '#':
            dfs(dx_, dy_)


# 최종 살아남은 양과 늑대 수
total_sheep = 0
total_wolves = 0

# 모든 좌표를 순회하면서 울타리로 둘러싸인 영역 탐색
for i in range(R):
    for j in range(C):
        if grid[i][j] != '#' and not visited[i][j]:
            # 한 영역에서 양과 늑대 수를 세기 위한 초기화
            sheep = 0
            wolves = 0

            # DFS 탐색 시작
            dfs(i, j)

            # 한 영역을 탐색한 후 결과 처리
            if sheep > wolves:
                total_sheep += sheep  # 양이 더 많으면 양이 살아남음
            else:
                total_wolves += wolves  # 늑대가 더 많으면 늑대가 살아남음

# 결과 출력
print(total_sheep, total_wolves)

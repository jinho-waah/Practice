import sys
from collections import deque
input = sys.stdin.readline

# 입력
N, L, R = map(int,input().split())
population = [list(map(int,input().split())) for _ in range(N)]

# 상하좌우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 인구 이동 진행 날 수
def bfs(x, y, visited):
    queue = deque([(x, y)])
    visited[x][y] = True
    #연합 리스트
    union = [(x, y)]
    union_population = population[x][y]

    while queue:
        #현재 위치
        cx, cy = queue.popleft()

        # 인접한 나라 탐색
        for i in range(4):
            nx, ny = cx + dx[i], cy + dy[i]

            # 범위 내에 있고 아직 방문하지 않았으며, 인구 차이가 L 이상 R 이하인 경우
            if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny]:
                if L <= abs(population[cx][cy] - population[nx][ny]) <= R:
                    visited[nx][ny] = True
                    queue.append((nx, ny))
                    union.append((nx, ny))
                    union_population += population[nx][ny]

    # 연합 인구 계산
    if len(union) > 1:
        new_population = union_population // len(union)
        for ux, uy in union:
            population[ux][uy] = new_population
        return True
    return False


# 인구 이동을 반복
days = 0
while True:
    visited = [[False] * N for _ in range(N)]
    moved = False

    for i in range(N):
        for j in range(N):
            if visited[i][j]: continue
            if bfs(i, j, visited):
                moved = True

    # 인구 이동이 없으면 종료
    if not moved:
        break
    days += 1

# 결과 출력
print(days)
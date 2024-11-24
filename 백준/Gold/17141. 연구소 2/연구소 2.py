import sys
input = sys.stdin.readline
from itertools import combinations
from collections import deque


def bfs(lab, virus_positions, empty_count, n):
    visited = [[-1] * n for _ in range(n)]
    queue = deque()

    # 초기 바이러스 위치 설정
    for x, y in virus_positions:
        queue.append((x, y))
        visited[x][y] = 0  # 시작 시간

    max_time = 0  # 바이러스가 퍼지는 데 걸린 시간
    filled_count = len(virus_positions)  # 바이러스가 퍼진 빈 칸 수
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    while queue:
        x, y = queue.popleft()
        current_time = visited[x][y]

        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] == -1:
                if lab[nx][ny] != 1:  # 빈 칸
                    filled_count += 1
                    max_time = max(max_time, current_time + 1)
                    visited[nx][ny] = current_time + 1
                    queue.append((nx, ny))

    # 모든 빈 칸이 채워졌는지 확인
    return max_time if filled_count == empty_count else float('inf')

def solve(n, m, lab):
    virus_positions = []  # 바이러스를 놓을 수 있는 칸
    empty_count = 0  # 빈 칸 개수

    # 연구소 초기 상태 분석
    for i in range(n):
        for j in range(n):
            if lab[i][j] == 2:
                virus_positions.append((i, j))
            if lab[i][j] != 1:
                empty_count += 1

    # 빈 칸이 없는 경우 바로 0 반환
    if empty_count == 0:
        return 0

    # M개의 바이러스 조합에 대해 최소 시간 계산
    min_time = float('inf')
    for selected_viruses in combinations(virus_positions, m):
        time = bfs(lab, selected_viruses, empty_count, n)
        min_time = min(min_time, time)

    return min_time if min_time != float('inf') else -1


# 입력 처리
N, M = map(int, input().split())
lab = [list(map(int, input().split())) for _ in range(N)]

# 결과 출력
print(solve(N, M, lab))
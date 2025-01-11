import sys
from collections import deque, defaultdict
input = sys.stdin.readline

def bfs(h, w, building, keys):
    # 방향 벡터 (상, 하, 좌, 우)
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    visited = [[False] * w for _ in range(h)]
    queue = deque()
    documents = 0

    # 현재 가지고 있는 열쇠 집합
    key_set = set(keys) if keys != "0" else set()

    # 대기 중인 문들 (열쇠가 없어서 못 연 문)
    doors = defaultdict(list)

    # 빌딩 가장자리에서 시작 가능한 위치 추가
    for i in range(h):
        for j in range(w):
            if i == 0 or i == h - 1 or j == 0 or j == w - 1:  # 가장자리
                if building[i][j] != '*' and not visited[i][j]:
                    queue.append((i, j))
                    visited[i][j] = True

    while queue:
        x, y = queue.popleft()

        cell = building[x][y]

        if cell == '$':  # 문서를 발견하면 개수 증가
            documents += 1
        elif 'a' <= cell <= 'z':  # 열쇠를 발견하면 추가하고 대기 중인 문을 처리
            key_set.add(cell)
            door_key = cell.upper()
            if door_key in doors:
                for door_x, door_y in doors[door_key]:
                    queue.append((door_x, door_y))
                del doors[door_key]
        elif 'A' <= cell <= 'Z':  # 문을 발견하면 열쇠가 있는지 확인
            if cell.lower() not in key_set:  # 열쇠가 없으면 대기
                doors[cell].append((x, y))
                continue

        # 인접한 칸 탐색
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < h and 0 <= ny < w and not visited[nx][ny] and building[nx][ny] != '*':
                visited[nx][ny] = True
                queue.append((nx, ny))

    return documents


def solve():
    t = int(input().strip())  # 테스트 케이스 개수

    for _ in range(t):
        h, w = map(int, input().split())
        building = [list(input().strip()) for _ in range(h)]
        keys = input().strip()

        print(bfs(h, w, building, keys))

solve()
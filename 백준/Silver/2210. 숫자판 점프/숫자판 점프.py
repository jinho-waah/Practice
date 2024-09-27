import sys
input = sys.stdin.readline

board = [list(map(int, input().split())) for _ in range(5)]

unique_numbers = set()

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# DFS 함수 정의
def dfs(x, y, number):
    # 6자리 숫자가 완성되면 집합에 추가하고 종료
    if len(number) == 6:
        unique_numbers.add(number)
        return

    # 상, 하, 좌, 우로 이동하며 탐색
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        # 그리드 범위를 벗어나지 않는지 확인
        if 0 <= nx < 5 and 0 <= ny < 5:
            # 다음 칸으로 이동하여 DFS 재귀 호출
            dfs(nx, ny, number + str(board[nx][ny]))

# 그리드의 각 좌표에서 DFS 탐색 시작
for i in range(5):
    for j in range(5):
        dfs(i, j, str(board[i][j]))

print(len(unique_numbers))
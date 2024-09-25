from collections import deque

# 방향 전환을 위한 북, 동, 남, 서 순서의 방향 벡터 (상, 우, 하, 좌)
dx = [-1, 0, 1, 0]  # 행 변화 (북, 동, 남, 서)
dy = [0, 1, 0, -1]  # 열 변화 (북, 동, 남, 서)

def turn(direction, c):
    if c == 'L':  # 왼쪽으로 90도 회전
        direction = (direction - 1) % 4
    else:  # 오른쪽으로 90도 회전
        direction = (direction + 1) % 4
    return direction

def simulate():
    time = 0  # 현재 시간
    x, y = 0, 0  # 뱀의 초기 위치 (행, 열)
    board[x][y] = 2  # 뱀이 있는 위치는 2로 표시
    direction = 1  # 초기 방향: 동쪽 (0: 북, 1: 동, 2: 남, 3: 서)
    snake = deque([(x, y)])  # 뱀의 몸 위치 (머리와 꼬리)
    idx = 0  # 방향 변환 정보 인덱스
    
    while True:
        # 다음 칸의 위치
        nx = x + dx[direction]
        ny = y + dy[direction]
        
        # 보드의 범위를 벗어나거나 자기 자신의 몸과 부딪히면 게임 종료
        if nx < 0 or nx >= N or ny < 0 or ny >= N or board[nx][ny] == 2:
            time += 1
            break
        
        # 뱀은 이동할 때 시간 1초 경과
        time += 1
        
        # 이동한 칸에 사과가 있다면, 꼬리는 움직이지 않고 머리만 늘림
        if board[nx][ny] == 1:
            board[nx][ny] = 2
            snake.append((nx, ny))
        else:  # 사과가 없으면 꼬리도 움직임
            board[nx][ny] = 2
            snake.append((nx, ny))
            tx, ty = snake.popleft()  # 꼬리 위치 제거
            board[tx][ty] = 0  # 꼬리가 있던 자리는 비어있음
        
        # 현재 시간이 방향 전환 시간과 일치하면 회전
        if idx < L and time == direction_info[idx][0]:
            direction = turn(direction, direction_info[idx][1])
            idx += 1
        
        # 머리 위치 갱신
        x, y = nx, ny
    
    return time

# 입력 처리
N = int(input())  # 보드 크기
K = int(input())  # 사과 개수
board = [[0] * N for _ in range(N)]  # 보드 초기화 (0: 빈 공간, 1: 사과, 2: 뱀)

# 사과 위치 입력
for _ in range(K):
    r, c = map(int, input().split())
    board[r - 1][c - 1] = 1  # 사과 위치는 1로 표시 (1행 1열을 0행 0열로 변환)

L = int(input())  # 방향 전환 정보 개수
direction_info = []  # 방향 전환 정보 리스트
for _ in range(L):
    X, C = input().split()
    direction_info.append((int(X), C))

# 결과 출력
print(simulate())

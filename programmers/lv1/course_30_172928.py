# 공원산책
def solution(park, routes):
    # 공원의 크기
    H = len(park)
    W = len(park[0])

    # 방향에 따른 이동 변화를 정의 (북, 남, 서, 동)
    direction = {
        "N": (-1, 0),
        "S": (1, 0),
        "W": (0, -1),
        "E": (0, 1)
    }

    # 시작 지점(S) 찾기
    start_x, start_y = 0, 0
    for i in range(H):
        for j in range(W):
            if park[i][j] == "S":
                start_x, start_y = i, j
                break

    # 명령을 하나씩 처리
    x, y = start_x, start_y
    for route in routes:
        op, n = route.split()
        n = int(n)
        dx, dy = direction[op]

        # 명령에 따라 이동할 좌표들을 미리 계산하고 확인
        new_x, new_y = x, y
        is_valid = True

        for step in range(n):
            new_x += dx
            new_y += dy

            # 경계를 벗어나거나 장애물에 부딪히면 명령 무시
            if not (0 <= new_x < H and 0 <= new_y < W) or park[new_x][new_y] == "X":
                is_valid = False
                break

        # 명령을 수행할 수 있으면 새로운 위치로 이동
        if is_valid:
            x, y = new_x, new_y

    return [x, y]

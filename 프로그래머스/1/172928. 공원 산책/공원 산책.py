def solution(park, routes):
    h = len(park)
    w = len(park[0])

    # 방향 정의: N/S/W/E → (dy, dx)
    direction_map = {
        'N': (-1, 0),
        'S': (1, 0),
        'W': (0, -1),
        'E': (0, 1)
    }

    # 시작 위치 찾기
    for i in range(h):
        for j in range(w):
            if park[i][j] == 'S':
                y, x = i, j

    for route in routes:
        dir, dist = route.split()
        dy, dx = direction_map[dir]
        dist = int(dist)

        ny, nx = y, x
        blocked = False

        for step in range(1, dist + 1):
            ty = y + dy * step
            tx = x + dx * step

            # 공원 밖으로 나가는지 확인
            if not (0 <= ty < h and 0 <= tx < w):
                blocked = True
                break

            # 장애물 있는지 확인
            if park[ty][tx] == 'X':
                blocked = True
                break

        # 경로에 문제 없으면 이동
        if not blocked:
            y += dy * dist
            x += dx * dist

    return [y, x]

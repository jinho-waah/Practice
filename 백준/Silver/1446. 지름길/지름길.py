import sys
input = sys.stdin.readline

def find_shortest_path(n, d, shortcuts):
    # 거리 테이블 초기화
    distance = [i for i in range(d + 1)]

    # 지름길 정보 정리
    shortcuts = [sc for sc in shortcuts if sc[1] <= d]  # 도착 지점이 D 이내인 지름길만 고려

    # 다익스트라 알고리즘
    for i in range(d + 1):
        if i > 0:  # 직선 도로로 이동하는 경우
            distance[i] = min(distance[i], distance[i - 1] + 1)

        for start, end, shortcut_length in shortcuts:
            if start == i:  # 현재 위치에서 시작하는 지름길
                distance[end] = min(distance[end], distance[i] + shortcut_length)

    return distance[d]


N, D = map(int, input().split())
shortcuts = [tuple(map(int, input().split())) for _ in range(N)]

print(find_shortest_path(N,D,shortcuts))

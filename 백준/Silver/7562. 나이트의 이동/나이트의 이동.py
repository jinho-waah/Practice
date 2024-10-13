import sys
from collections import defaultdict, deque
from statistics import mean
import heapq
from itertools import combinations

input = sys.stdin.readline
import math
sys.setrecursionlimit(2000)


# 나이트가 이동할 수 있는 8가지 방향
dx = [-2, -1, 1, 2, 2, 1, -1, -2]
dy = [1, 2, 2, 1, -1, -2, -2, -1]


# BFS 함수 정의
def bfs(l, start, end):
    # 체스판 크기 l, 시작 좌표 start, 도착 좌표 end
    queue = deque([start])
    visited = [[False] * l for _ in range(l)]
    visited[start[0]][start[1]] = True
    dist = [[0] * l for _ in range(l)]  # 이동 거리를 저장하는 배열

    while queue:
        x, y = queue.popleft()

        # 도착 지점에 도달한 경우 이동 거리를 반환
        if (x, y) == end:
            return dist[x][y]

        # 나이트가 이동할 수 있는 모든 방향에 대해 BFS 탐색
        for i in range(8):
            nx, ny = x + dx[i], y + dy[i]

            if 0 <= nx < l and 0 <= ny < l and not visited[nx][ny]:
                visited[nx][ny] = True
                dist[nx][ny] = dist[x][y] + 1
                queue.append((nx, ny))

    return -1  # 도착할 수 없는 경우는 없지만 안전하게 반환


# 테스트 케이스 입력 받기
t = int(input())  # 테스트 케이스 수

for _ in range(t):
    l = int(input())  # 체스판 한 변의 길이
    start = tuple(map(int, input().split()))  # 시작 위치
    end = tuple(map(int, input().split()))  # 목표 위치

    # 시작점과 목표점이 같은 경우 바로 0을 출력
    if start == end:
        print(0)
    else:
        # BFS를 이용해 최소 이동 횟수를 계산
        print(bfs(l, start, end))
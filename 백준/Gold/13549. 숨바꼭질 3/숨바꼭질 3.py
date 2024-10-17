import sys
from collections import defaultdict, deque
from statistics import mean
import heapq
from itertools import combinations
import math
sys.setrecursionlimit(2000)

input = sys.stdin.readline


subin_x, brother_x = map(int, input().split())


def dfs(N, K):
    # 방문 여부를 기록할 리스트 (0~100000)
    visited = [False] * 100001
    # 큐를 초기화, 시작 위치와 시간을 저장
    queue = deque([(N, 0)])

    # BFS 탐색
    while queue:
        current, time = queue.popleft()

        # 동생을 찾았으면 시간을 반환
        if current == K:
            return time

        # 이동 가능한 3가지 경우
        # 순간이동 (0초)
        if 0 <= current * 2 <= 100000 and not visited[current * 2]:
            queue.appendleft((current * 2, time))  # 우선 처리
            visited[current * 2] = True

        # X-1로 이동 (1초)
        if 0 <= current - 1 <= 100000 and not visited[current - 1]:
            queue.append((current - 1, time + 1))
            visited[current - 1] = True

        # X+1로 이동 (1초)
        if 0 <= current + 1 <= 100000 and not visited[current + 1]:
            queue.append((current + 1, time + 1))
            visited[current + 1] = True


print(dfs(subin_x, brother_x))
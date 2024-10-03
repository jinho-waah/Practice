import sys
from collections import defaultdict, deque
from statistics import mean
from itertools import combinations
input = sys.stdin.readline
sys.setrecursionlimit(2000)

# 입력 처리
N, M = map(int, input().split())
city = [list(map(int, input().split())) for _ in range(N)]

# 집과 치킨집의 좌표를 저장
houses = []
chicken_stores = []

for r in range(N):
    for c in range(N):
        if city[r][c] == 1:
            houses.append((r, c))
        elif city[r][c] == 2:
            chicken_stores.append((r, c))

# 치킨 거리 계산 함수
def get_chicken_distance(houses, selected_chickens):
    total_distance = 0
    for hr, hc in houses:
        min_distance = float('inf')
        for cr, cc in selected_chickens:
            distance = abs(hr - cr) + abs(hc - cc)
            min_distance = min(min_distance, distance)
        total_distance += min_distance
    return total_distance

# 가능한 모든 치킨집 조합을 고려하여 최소 치킨 거리 계산
min_city_chicken_distance = float('inf')

for selected_chickens in combinations(chicken_stores, M):
    city_chicken_distance = get_chicken_distance(houses, selected_chickens)
    min_city_chicken_distance = min(min_city_chicken_distance, city_chicken_distance)

# 결과 출력
print(min_city_chicken_distance)
import sys

input = sys.stdin.readline

# 입력 처리
N, M = map(int, input().split())
coords = list(map(int, input().split()))

negative_coords = []
positive_coords = []

# 좌표를 음수와 양수로 나누어 처리
for coord in coords:
    if coord < 0:
        negative_coords.append(coord)
    else:
        positive_coords.append(coord)

# 음수와 양수를 각각 정렬
negative_coords.sort()  # 음수는 오름차순 정렬 (가장 먼 거리가 마지막에 위치)
positive_coords.sort(reverse=True)  # 양수는 내림차순 정렬 (가장 먼 거리가 첫 번째에 위치)

walk = 0

# 음수 좌표 처리: 가장 먼 곳부터 한 번에 최대 M권씩 처리
for i in range(0, len(negative_coords), M):
    walk += abs(negative_coords[i]) * 2

# 양수 좌표 처리: 가장 먼 곳부터 한 번에 최대 M권씩 처리
for i in range(0, len(positive_coords), M):
    walk += positive_coords[i] * 2

# 최적화: 마지막으로 가장 먼 거리는 단방향만 이동
# 음수와 양수 좌표 중 가장 먼 위치를 한 번만 이동
if negative_coords and positive_coords:
    max_distance = max(abs(negative_coords[0]), positive_coords[0])
elif negative_coords:
    max_distance = abs(negative_coords[0])
elif positive_coords:
    max_distance = positive_coords[0]
else:
    max_distance = 0

walk -= max_distance

print(walk)

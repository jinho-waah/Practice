import sys
input = sys.stdin.readline

def reverse(given_array, i, j):
    for x in range(i, i + 3):
        for y in range(j, j + 3):
            given_array[x][y] = 1 - given_array[x][y]

# 입력 처리
N, M = map(int, input().split())
array_before = [list(map(int, input().strip())) for _ in range(N)]
array_after = [list(map(int, input().strip())) for _ in range(N)]

# 변환 횟수
count = 0

# 3x3 변환 수행
for i in range(N - 2):
    for j in range(M - 2):
        # 현재 위치에서 값이 다르면 3x3 변환 수행
        if array_before[i][j] != array_after[i][j]:
            reverse(array_before, i, j)
            count += 1

# 최종 상태 확인
is_possible = True
for i in range(N):
    if array_before[i] != array_after[i]:
        is_possible = False
        break

if is_possible:
    print(count)
else:
    print(-1)

import sys
input = sys.stdin.readline

def is_possible(houses, n, c, distance):
    # 첫 번째 집에 공유기 설치
    count = 1
    last_position = houses[0]

    for i in range(1, n):
        if houses[i] - last_position >= distance:
            count += 1
            last_position = houses[i]
            if count >= c:  # 필요한 개수만큼 설치 완료
                return True

    return False

def find_max_distance(n, c, houses):
    # 집 좌표 정렬
    houses.sort()

    # 이진 탐색 범위 설정
    left = 1  # 최소 거리
    right = houses[-1] - houses[0]  # 최대 거리
    result = 0

    while left <= right:
        mid = (left + right) // 2

        if is_possible(houses, n, c, mid):
            result = mid  # 가능한 거리 저장
            left = mid + 1  # 더 큰 거리 탐색
        else:
            right = mid - 1  # 더 작은 거리 탐색

    return result

# 입력 처리
n, c = map(int, input().split())
houses = [int(input().strip()) for _ in range(n)]

# 결과 출력
print(find_max_distance(n, c, houses))
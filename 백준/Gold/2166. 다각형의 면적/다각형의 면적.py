import sys
input = sys.stdin.readline

def calculate_polygon_area(points):
    n = len(points)
    area = 0

    # 신발끈 공식 계산
    for i in range(n):
        x1, y1 = points[i]
        x2, y2 = points[(i + 1) % n]  # 다음 점 (폐합 조건)
        area += x1 * y2 - y1 * x2

    return abs(area) / 2

# 입력 처리
N = int(input().strip())

nodes = [tuple(map(int, input().split())) for _ in range(N)]

area = calculate_polygon_area(nodes)
print(f"{area:.1f}")
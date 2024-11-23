import sys
input = sys.stdin.readline


def draw_stars(n):
    if n == 3:
        return ["  *  ", " * * ", "*****"]

    # 이전 단계의 별 패턴
    prev = draw_stars(n // 2)
    length = len(prev)

    # 상단: 이전 패턴
    top = [" " * length + line + " " * length for line in prev]

    # 하단: 이전 패턴 두 개를 나란히 배치
    bottom = [line + " " + line for line in prev]

    return top + bottom


# 입력 처리
N = int(input().strip())

# 별 패턴 생성
stars = draw_stars(N)

# 출력
print("\n".join(stars))
# 이 문제도 그냥 풀면 런타임 에러가 뜰 수 있음
# 방법은 여러가지가 있겠지만
# 4번 문제 같은 경우 숫자의 범위가 생각보다 좁기 때문에 결과 값을 저장하면 어떨까 싶어서 채택한 방법


#저장을 위한 3차원 배열 초기화 (-1로 초기화)
storage = [[[-1 for _ in range(51)] for _ in range(51)] for _ in range(51)]


# 재귀함수 w(a, b, c) 정의
def w(a, b, c):
    # 조건 1: a, b, c 중 하나라도 0 이하이면 1을 반환
    if a <= 0 or b <= 0 or c <= 0:
        return 1

    # 조건 2: a, b, c 중 하나라도 20을 초과하면 w(20, 20, 20) 반환
    if a > 20 or b > 20 or c > 20:
        return w(20, 20, 20)

    # 메모이제이션 체크
    if storage[a][b][c] != -1:
        return storage[a][b][c]

    # 조건 3: a < b < c 이면
    if a < b and b < c:
        storage[a][b][c] = w(a, b, c - 1) + w(a, b - 1, c - 1) - w(a, b - 1, c)
    else:
        # 그 외의 경우
        storage[a][b][c] = w(a - 1, b, c) + w(a - 1, b - 1, c) + w(a - 1, b, c - 1) - w(a - 1, b - 1, c - 1)

    return storage[a][b][c]


# 입력 받기 및 출력 처리
while True:
    a, b, c = map(int, input().split())

    # 입력이 -1 -1 -1이면 종료
    if a == -1 and b == -1 and c == -1:
        break

    # w(a, b, c)의 값을 출력
    print(f"w({a}, {b}, {c}) = {w(a, b, c)}")
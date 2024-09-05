def zigzag(N, r, c):
    if N == 0:      #N = 0이면 0이니 여태 구한 값을 누적 시키면 된다
        return 0

    # 2^(N-1) X 2^(N-1)로 4등 분 후 순서대로 방문
    # 즉 1,2,3,4 왼쪽 위부터 지그 재그 모양으로 순서대로 지정 하면
    # 각 구역을 탐색할때 넓이를 더해준다고 생각하면 된다.
    half = 2 ** (N -1)
    if r < half and c < half:       #첫번째 순서이므로 더해줄 넓이가 없다
        # 1사분면 (왼쪽 위)
        return zigzag(N - 1, r, c)
    elif r < half and c >= half:    #두번째 순서이므로 한분면의 넓이 만큼 더해주면 된다.
        # 2사분면 (오른쪽 위)
        return half * half + zigzag(N - 1, r, c - half)
    elif r >= half and c < half:    #세번째 순서이므로 두분면의 넓이 만큼 더해주면 된다.
        # 3사분면 (왼쪽 아래)
        return 2 * half * half + zigzag(N - 1, r - half, c)
    else:                           #네번째 순서이므로 3분면의 넓이 만큼 더해주면 된다.
        # 4사분면 (오른쪽 아래)
        return 3 * half * half + zigzag(N - 1, r - half, c - half)
# 입력 받기
N, r, c = map(int, input().split())

# 결과 출력
print(zigzag(N, r, c))

import sys
input = sys.stdin.readline

DIRECTIONS = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]

def move_fireballs(fireballs, N):
    new_positions = {}
    for r, c, m, s, d in fireballs:
        # 새로운 위치 계산 (격자 밖으로 나가면 연결됨)
        nr = (r + DIRECTIONS[d][0] * s) % N
        nc = (c + DIRECTIONS[d][1] * s) % N
        if (nr, nc) not in new_positions:
            new_positions[(nr, nc)] = []
        new_positions[(nr, nc)].append((m, s, d))
    return new_positions

def merge_fireballs(grid):
    new_fireballs = []
    for (r, c), fireballs in grid.items():
        if len(fireballs) == 1:
            # 파이어볼이 하나만 있으면 그대로 유지
            new_fireballs.append((r, c) + fireballs[0])
        else:
            # 여러 파이어볼 병합
            total_m = sum(f[0] for f in fireballs)
            total_s = sum(f[1] for f in fireballs)
            count = len(fireballs)
            new_m = total_m // 5
            new_s = total_s // count
            if new_m > 0:
                # 방향 결정
                all_even = all(f[2] % 2 == 0 for f in fireballs)
                all_odd = all(f[2] % 2 == 1 for f in fireballs)
                directions = [0, 2, 4, 6] if all_even or all_odd else [1, 3, 5, 7]
                for d in directions:
                    new_fireballs.append((r, c, new_m, new_s, d))
    return new_fireballs

def solve():
    # 입력 처리
    N, M, K = map(int, input().split())
    fireballs = []
    for _ in range(M):
        r, c, m, s, d = map(int, input().split())
        fireballs.append((r - 1, c - 1, m, s, d))  # 0-based indexing

    # K번 이동 및 병합 반복
    for _ in range(K):
        # 파이어볼 이동
        grid = move_fireballs(fireballs, N)
        # 파이어볼 병합 및 분리
        fireballs = merge_fireballs(grid)

    # 남아있는 파이어볼 질량 합 계산
    total_mass = sum(f[2] for f in fireballs)
    print(total_mass)

solve()
import sys
input = sys.stdin.readline
from collections import defaultdict, deque

def propagate_praise(n, m, hierarchy, praises):
    # 트리 구조 생성
    tree = defaultdict(list)
    for employee, manager in enumerate(hierarchy, start=1):
        if manager != -1:
            tree[manager].append(employee)

    # 칭찬 초기화
    praise = [0] * (n + 1)

    # 초기 칭찬 적용
    for i, w in praises:
        praise[i] += w

    # BFS로 칭찬 전파
    queue = deque([1])  # 사장부터 시작
    while queue:
        current = queue.popleft()
        for subordinate in tree[current]:
            praise[subordinate] += praise[current]  # 현재 칭찬을 부하에게 전달
            queue.append(subordinate)

    return praise[1:]  # 1번부터 n번까지의 칭찬 점수 반환


# 입력 처리
N, M = map(int, input().split())
hierarchy = list(map(int, input().split()))
praises = [tuple(map(int, input().split())) for _ in range(M)]

# 결과 출력
result = propagate_praise(N, M, hierarchy, praises)
print(" ".join(map(str, result)))
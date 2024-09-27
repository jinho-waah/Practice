import sys
input = sys.stdin.readline

# 유니온-파인드 자료구조의 find 함수 (경로 압축 최적화 포함)
def find(parent, x):
    # 현재 노드 x가 자기 자신을 부모로 가리키고 있지 않다면 (즉, 루트가 아니라면)
    if parent[x] != x:
        # 루트를 찾아서 parent[x]에 기록 (경로 압축)
        parent[x] = find(parent, parent[x])
    # 루트를 반환
    return parent[x]


# 유니온-파인드 자료구조의 union 함수 (랭크 최적화 포함)
def union(parent, rank, a, b):
    # a와 b의 루트를 각각 찾는다
    root_a = find(parent, a)
    root_b = find(parent, b)

    # 루트가 같지 않다면, 두 집합을 합친다
    if root_a != root_b:
        # rank(트리의 깊이)를 비교해서 더 작은 트리를 큰 트리 밑에 붙인다
        if rank[root_a] < rank[root_b]:
            parent[root_a] = root_b  # a의 트리를 b의 트리 밑에 붙임
        elif rank[root_a] > rank[root_b]:
            parent[root_b] = root_a  # b의 트리를 a의 트리 밑에 붙임
        else:
            parent[root_b] = root_a  # 랭크가 같으면 한쪽 트리 밑으로 붙이고, 랭크 증가
            rank[root_a] += 1


N = int(input())
M = int(input())

edges = []
for _ in range(M):
    a, b, c = map(int, input().split())  # a컴퓨터와 b컴퓨터를 연결하는데 드는 비용 c
    edges.append((c, a, b))     # 모든 간선을 저장하는데 비용에 따라 정렬하기 위해 c를 앞에 배치

edges.sort()

# 유니온-파인드 준비
parent = [i for i in range(N + 1)]  # 처음엔 각 노드가 자기 자신이 부모
rank = [0] * (N + 1)  # 트리의 깊이를 추적하기 위한 rank 배열

# 크루스칼 알고리즘으로 최소 스패닝 트리(MST) 계산
mst_cost = 0  # MST의 총 비용
selected_edges = 0  # 선택된 간선의 수

for edge in edges:
    cost, a, b = edge
    # 두 노드가 같은 집합에 있지 않으면 연결 (사이클이 없을 때만)
    if find(parent, a) != find(parent, b):
        union(parent, rank, a, b)
        mst_cost += cost
        selected_edges += 1
    # N-1개의 간선을 선택했으면 모든 노드를 연결한 것이므로 종료
    if selected_edges == N - 1:
        break

# 결과 출력
print(mst_cost)
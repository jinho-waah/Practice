import sys
from collections import defaultdict, deque
input = sys.stdin.readline

# 입력
N, M= map(int,input().split())
graph = defaultdict(list)

# 그래프와 진입 차수 배열 설정
in_degree = [0] * (N + 1)
for _ in range(M):
    A, B = map(int, input().split())
    graph[A].append(B)
    in_degree[B] += 1

# 위상 정렬 함수
def topological_sort():
    queue = deque()
    result = []

    # 진입 차수가 0인 노드를 큐에 삽입
    for i in range(1, N + 1):
        if in_degree[i] == 0:
            queue.append(i)

    # 큐에서 노드를 하나씩 꺼내며 위상 정렬 수행
    while queue:
        node = queue.popleft()
        result.append(node)

        for neighbor in graph[node]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    return result


# 결과 출력
sorted_order = topological_sort()
print(" ".join(map(str, sorted_order)))
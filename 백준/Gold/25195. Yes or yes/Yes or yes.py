import sys
from collections import defaultdict, deque

input = sys.stdin.readline

# 입력 처리
N, M = map(int, input().split())

graph = defaultdict(list)

# 그래프 구성
for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)

# 팬클럽이 존재하는 정점 정보 입력
S = int(input())
fanclub_nodes = set(map(int, input().split()))

# BFS로 1번 정점에서 도달 가능한 모든 노드를 찾음
def dfs(start):
    stack = [start]
    visited = [False] * (N + 1)

    while stack:
        node = stack.pop()

        # 이미 방문했거나 팬클럽 노드인 경우
        if visited[node] or node in fanclub_nodes:
            continue

        # 현재 노드를 방문 처리
        visited[node] = True

        # 리프 노드에 도달했을 경우, 팬클럽이 없는 리프 노드라면 'yes'를 출력하고 종료
        if not graph[node]:
            print("yes")
            return

        # 다음 노드를 탐색하기 위해 스택에 추가
        for neighbor in graph[node]:
            if not visited[neighbor]:
                stack.append(neighbor)

    # 모든 탐색을 마쳤음에도 팬클럽이 없는 리프 노드를 방문하지 못한 경우
    print("Yes")

# 시작 노드 1에서 DFS 탐색 시작
dfs(1)
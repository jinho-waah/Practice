from collections import deque, defaultdict
import sys
input = sys.stdin.readline

def is_bipartite(v, graph):
    color = [0] * (v + 1)  # 0: 미방문, 1: 색1, -1: 색2

    def bfs(start):
        queue = deque([start])
        color[start] = 1  # 시작 정점을 색1로 칠함
        while queue:
            current = queue.popleft()
            for neighbor in graph[current]:
                if color[neighbor] == 0:  # 아직 방문하지 않은 정점
                    color[neighbor] = -color[current]  # 반대 색으로 칠함
                    queue.append(neighbor)
                elif color[neighbor] == color[current]:  # 인접 정점이 같은 색
                    return False
        return True

    # 그래프의 모든 연결 요소 탐색
    for i in range(1, v + 1):
        if color[i] == 0:  # 방문하지 않은 정점이면 BFS 시작
            if not bfs(i):
                return False
    return True

# 입력 처리
k = int(input().strip())  # 테스트 케이스 개수
results = []

for _ in range(k):
    v, e = map(int, input().split())  # 정점, 간선 개수
    graph = defaultdict(list)

    for _ in range(e):
        u, w = map(int, input().split())  # 간선 정보 처리 (u, w 사용)
        graph[u].append(w)
        graph[w].append(u)

    # 이분 그래프 판별
    results.append("YES" if is_bipartite(v, graph) else "NO")

# 결과 출력
for result in results:
    print(result)

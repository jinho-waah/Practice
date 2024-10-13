N = int(input())  # 도시의 수
W = [list(map(int, input().split())) for _ in range(N)]  # 비용 행렬

# 아주 큰 값으로 초기화 (경로 비용 최소화를 위해)
INF = float('inf')
min_cost = INF

# 방문한 도시들을 체크하기 위한 배열
visited = [False] * N

def tsp(current_city, count, cost, start_city):
    global min_cost

    # 모든 도시를 방문한 경우, 출발 도시로 돌아오는 비용을 더해 최소 비용을 갱신
    if count == N and W[current_city][start_city] != 0:
        min_cost = min(min_cost, cost + W[current_city][start_city])
        return

    # 현재 도시에서 다른 도시로 이동
    for next_city in range(N):
        if not visited[next_city] and W[current_city][next_city] != 0:
            visited[next_city] = True
            tsp(next_city, count + 1, cost + W[current_city][next_city], start_city)
            visited[next_city] = False

# 모든 도시를 출발 도시로 삼아 최소 비용 계산
for i in range(N):
    visited[i] = True
    tsp(i, 1, 0, i)
    visited[i] = False

print(min_cost)

import sys
from collections import deque
input = sys.stdin.readline

N, K = map(int, input().split())


queue = deque([N])

visited = [-1] * 100001
visited[N] = 0


while queue:
    current = queue.popleft()

    if current == K:
        break

    for next in (current - 1, current + 1, current * 2):
        if 0 <= next <= 100000 and visited[next] == -1:
            visited[next] = visited[current] + 1
            queue.append(next)

print(visited[K])
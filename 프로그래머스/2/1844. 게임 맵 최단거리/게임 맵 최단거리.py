from collections import deque

def solution(maps):
    n = len(maps)        # 행 길이
    m = len(maps[0])     # 열 길이
    visited = [[False]*m for _ in range(n)]  # 방문 여부
    queue = deque()
    
    # 시작 지점: (0, 0), 거리: 1
    queue.append((0, 0, 1))
    visited[0][0] = True
    
    # 방향: 동, 서, 남, 북
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    
    while queue:
        x, y, dist = queue.popleft()
        
        # 도착 지점에 도달하면 거리 반환
        if x == n - 1 and y == m - 1:
            return dist
        
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            
            # 맵 안에 있고, 갈 수 있는 길이며, 방문하지 않은 경우
            if 0 <= nx < n and 0 <= ny < m and maps[nx][ny] == 1 and not visited[nx][ny]:
                visited[nx][ny] = True
                queue.append((nx, ny, dist + 1))
    
    # 도달할 수 없는 경우
    return -1
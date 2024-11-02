import sys
from collections import deque
input = sys.stdin.readline

# 입력
S = int(input().strip())

# BFS를 위한 큐, (현재 화면 이모티콘 수, 클립보드 이모티콘 수, 시간)
queue = deque([(1, 0, 0)])

# 방문한 상태 (화면 이모티콘 수, 클립보드 이모티콘 수)
visited = set()
visited.add((1, 0))

while queue:
    screen, clipboard, time = queue.popleft()

    # 목표 이모티콘 수에 도달한 경우
    if screen == S:
        print(time)
        break

    # 연산 1: 화면에 있는 이모티콘을 모두 클립보드에 복사
    if (screen, screen) not in visited:
        visited.add((screen, screen))
        queue.append((screen, screen, time + 1))

    # 연산 2: 클립보드에 있는 이모티콘을 화면에 붙여넣기 (클립보드에 내용이 있을 경우)
    if clipboard > 0 and (screen + clipboard, clipboard) not in visited:
        visited.add((screen + clipboard, clipboard))
        queue.append((screen + clipboard, clipboard, time + 1))

    # 연산 3: 화면에서 이모티콘 하나 삭제 (화면에 이모티콘이 1개 이상 있을 경우)
    if screen > 1 and (screen - 1, clipboard) not in visited:
        visited.add((screen - 1, clipboard))
        queue.append((screen - 1, clipboard, time + 1))




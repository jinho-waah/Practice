from collections import deque

def solution(priorities, location):
    queue = deque([(i, p) for i, p in enumerate(priorities)])
    answer = 0

    while queue:
        cur = queue.popleft()
        if any(cur[1] < other[1] for other in queue):
            queue.append(cur)  # 뒤로 보내
        else:
            answer += 1  # 실행됨!
            if cur[0] == location:
                return answer

import sys
from collections import deque
input = sys.stdin.readline


case = int(input())

for _ in range(case):
    N, M = map(int, input().split())
    doc = list(map(int,input().split()))

    queue = deque([(i, priority) for i, priority in enumerate(doc)])
    print_order = 0
    
    while queue:
        current = queue.popleft()

        if any(current[1] < q[1] for q in queue):
            queue.append(current)

        else:
            print_order += 1
            if current[0] == M:
                print(print_order)
                break
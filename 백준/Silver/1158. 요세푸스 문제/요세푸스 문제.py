import sys
from collections import deque
input = sys.stdin.readline


N, K = map(int, input().split())
deq = deque(i for i in range(1, N+1))
result = []

while deq:
    deq.rotate(-(K-1))
    result.append(deq.popleft())

# 결과 출력
print("<" + ", ".join(map(str, result)) + ">")
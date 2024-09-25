import sys
from collections import deque
input = sys.stdin.readline


N = int(input())
deq = deque((index+1, value) for index, value in enumerate(map(int,input().split())))
result = []

while deq:
    idx, val = deq.popleft()
    result.append(idx)
    if deq:
        if val > 0:
            deq.rotate(-(val - 1))
        else:
            deq.rotate(-val)
print(" ".join(map(str, result)))
from collections import deque
import sys

input = sys.stdin.readline

bomb_deq = deque(input().strip())
bomb = input().strip()

stack = []

while bomb_deq:
    stack.append(bomb_deq.popleft()) 

    if ''.join(stack[-len(bomb):]) == bomb:
        for _ in range(len(bomb)):
            stack.pop()

if stack:
    print(''.join(stack))
else:
    print("FRULA")
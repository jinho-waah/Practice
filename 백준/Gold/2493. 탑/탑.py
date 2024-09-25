from collections import deque
import sys

input = sys.stdin.readline

N = int(input())
tower_list = list(map(int, input().split()))

answer = [0] * N

stack = []

for i in range(N):
    while stack and stack[-1][1] < tower_list[i]:
        stack.pop()

    if stack:
        answer[i] = stack[-1][0]

    stack.append((i + 1, tower_list[i]))

print(" ".join(map(str, answer)))

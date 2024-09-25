import sys

input = sys.stdin.readline


left_stack = list(input().strip())
right_stack = []
N = int(input())


for _ in range(N):
    query = input()

    if query.startswith("L"):
        if left_stack:
            right_stack.append(left_stack.pop())
    elif query.startswith("D"):
        if right_stack:
            left_stack.append(right_stack.pop())
    elif query.startswith("B"):
        if left_stack:
            left_stack.pop()
    elif query.startswith("P"):
        _, value = query.split()
        left_stack.append(value)

print(''.join(left_stack + right_stack[::-1]))
import sys

input = sys.stdin.readline


N = int(input())
stack = []
result = []

for _ in range(N):
    query = input()

    if query.startswith("push"):
        _, value = query.split()
        stack.append(value)
    elif query.startswith("pop"):
        if len(stack) == 0:
            print(-1)
        else:
            print(stack.pop())
    elif query.startswith("size"):
        print(len(stack))
    elif query.startswith("empty"):
        if len(stack) == 0:
            print(1)
        else:
            print(0)
    elif query.startswith("top"):
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[-1])
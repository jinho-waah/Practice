from collections import deque
import sys

N = int(input())

query_list = [input() for _ in range(N)]

storage = deque()
# print(query_list)

for query_string in query_list:
    if ' ' in query_string:
        query, n = query_string.split()
    else:
        query = query_string

    if query == "push_front":
        storage.appendleft(n)
    elif query == "push_back":
        storage.append(n)
    elif query == "pop_front":
        if len(storage) == 0:
            print(-1)
        else:
            print(storage[0])
            storage.popleft()
    elif query == "pop_back":
        if len(storage) == 0:
            print(-1)
        else:
            print(storage[-1])
            storage.pop()
    elif query == "size":
        print(len(storage))
    elif query == "empty":
        if len(storage) == 0:
            print(1)
        else:
            print(0)
    elif query == "front":
        if len(storage) > 0:
            print(storage[0])
        else:
            print(-1)
    elif query == "back":
        if len(storage) > 0:
            print(storage[-1])
        else:
            print(-1)

# print(storage)

#
# N = int(input())
#
# queries = [input() for _ in range(N)]
#
# manipulated_queries = []
# result = ""
# # print(queries)
#
# for query in queries:
#     if query != '3':
#         manipulated_queries.append(query)
#     if len(manipulated_queries) > 0 and query == '3':
#         manipulated_queries.pop()
#
# # print(manipulated_queries)
#
# for query in manipulated_queries:
#     num, c = query.split()
#     if num == "1":
#         result = result + c
#     else:
#         result = c + result
#
# print(result)


from sys import stdin
from collections import deque

now = deque()
n = int(stdin.readline())
stack = []
for _ in range(n):
    op = list(map(str, stdin.readline().split()))
    if op[0] == '1':
        now.append(op[1])
        stack.append('back')
    elif op[0] == '2':
        now.appendleft(op[1])
        stack.append('front')
    else:
        if stack:
            value = stack.pop()
            if value == 'back':
                now.pop()
            else:
                now.popleft()

if len(now) == 0:
    print('0')
else:
    print("".join(now))
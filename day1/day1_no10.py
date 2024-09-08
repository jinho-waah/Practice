# a + ( n - 1 ) * d를 떠올렸으면 반쯤 성공인듯 한데..
#
#

# num = int(input())
#
# list_set = [list(map(int, input().split())) for _ in range(num)]
#
# for a,d,x in list_set:
#     if a > x:
#         print(1, x)
#     else:
#         level = 2
#         left_node = a + 1
#         right_node = a + (a + d)
#
#         while True:
#             if left_node <= x <= right_node:
#                 break
#             level +=1
#             left_node = right_node + 1
#             right_node = right_node + a + (level-1) * d
#
#         print(level, x - left_node + 1)

import sys
# input = sys.stdin.readline
num = int(input())

for _ in range(num):
    a, d, x = map(int, input().split())

    if x < a:
        print(1, x)
        continue

    level = 1
    start = a
    end = a
    while end < x:
        level += 1
        start = end + 1
        end = start + a + (level - 1) * d - 1

    print(level, x - start + 1)


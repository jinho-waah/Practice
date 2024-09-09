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
# num = int(input())
#
# for _ in range(num):
#     a, d, x = map(int, input().split())
#
#     if x < a:
#         print(1, x)
#         continue
#
#     level = 1
#     start = a
#     end = a
#     while end < x:
#         level += 1
#         start = end + 1
#         end = start + a + (level - 1) * d - 1
#
#     print(level, x - start + 1)


def get_left(a, d, n):
    return (n - 1) * (2 * a + (n - 2) * d) // 2 + 1

import sys
input = sys.stdin.readline

num = int(input())

for _ in range(num):
    a, d, x = map(int, input().split())

    low = 1
    high = 10 ** 6
    level = 1
    left = 1

    # 이분 탐색을 통해 층(level)을 찾는다
    while low <= high:
        level = (low + high) // 2
        left = get_left(a, d, level)

        if left > x:
            high = level - 1  # 범위를 좁힌다 (high를 줄인다)
        elif left <= x:
            if get_left(a, d, level + 1) > x:  # x가 해당 층에 속하면 종료
                break
            low = level + 1  # 범위를 좁힌다 (low를 늘린다)

    # 해당 층에서 x가 몇 번째인지 계산
    block_index = x - left + 1

    print(level, block_index)





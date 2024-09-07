# a + ( n - 1 ) * d를 떠올렸으면 반쯤 성공인듯 한데..
#
#

num = int(input())

list_set = [list(map(int, input().split())) for _ in range(num)]

for a,d,x in list_set:
    level = 1
    # while True:
    #     if 1 + (level - 1) * d
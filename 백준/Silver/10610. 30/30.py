import sys
from collections import defaultdict, deque
input = sys.stdin.readline
sys.setrecursionlimit(2000)

# 입력 처리
N = int(input().strip())
N_list = [int(digit) for digit in str(N)]
N_list.sort(reverse=True)

result = -1
if N_list[-1] == 0 and sum(N_list) % 3 == 0:
    result = int(''.join(map(str, N_list)))

print(result)
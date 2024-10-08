import sys
from collections import defaultdict, deque
from statistics import mean
import heapq
from itertools import combinations

input = sys.stdin.readline
import math
sys.setrecursionlimit(2000)


# 입력 처리
N = int(input().strip())
nicknames = [input().strip() for _ in range(N)]

nickname_count = defaultdict(int)
used_prefixes = set()
result = []

for nickname in nicknames:
    nickname_count[nickname] += 1
    count = nickname_count[nickname]

    prefix = ""
    unique_prefix_found = False
    for i in range(1, len(nickname) + 1):
        prefix = nickname[:i]
        if prefix not in used_prefixes and not unique_prefix_found:
            used_prefixes.add(prefix)
            result.append(prefix)
            unique_prefix_found = True
        if unique_prefix_found:
            used_prefixes.add(prefix)

    # 고유 접두사를 못 찾았다면
    if not unique_prefix_found:
        if count == 1:
            result.append(nickname)
        else:
            result.append(f"{nickname}{count}")

for pre in result:
    print(pre)
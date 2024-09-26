import heapq
import sys
from collections import defaultdict
input = sys.stdin.readline

# 입력 처리
n = int(input())

for _ in range(n):
    wear_dict = defaultdict(list)

    # 의상 아이템과 그 종류를 입력받아 딕셔너리에 추가
    for _ in range(int(input())):
        item, part = input().split()
        wear_dict[part].append(item)

    # 각 의상 종류에 따른 조합 계산
    tmp = 1
    for items in wear_dict.values():
        tmp *= (len(items) + 1)  # 각 의상 종류에서 고를 수 있는 경우의 수는 (해당 종류의 아이템 개수 + 1)

    # 모든 의상 종류에서 아무것도 선택하지 않은 경우를 제외
    print(tmp - 1)
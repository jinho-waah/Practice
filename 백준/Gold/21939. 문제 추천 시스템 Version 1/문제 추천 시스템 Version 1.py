import heapq
import sys
from collections import defaultdict
input = sys.stdin.readline

N = int(input())

# 문제 정보를 저장할 힙
max_heap = []  # 최대 힙 (어려운 문제 찾기)
min_heap = []  # 최소 힙 (쉬운 문제 찾기)
problem_dict = {}  # 문제 번호를 키로, 난이도를 값으로 저장하는 딕셔너리

for _ in range(N):
    P, L = map(int, input().split())
    heapq.heappush(max_heap, (-L, -P))  # 난이도와 문제 번호를 음수로 저장
    heapq.heappush(min_heap, (L, P))  # 난이도와 문제 번호를 양수로 저장
    problem_dict[P] = L  # 문제 번호를 키로, 난이도를 값으로 저장

# 명령어 처리
M = int(input())
for _ in range(M):
    command = input().split()

    if command[0] == 'add':
        P, L = int(command[1]), int(command[2])
        heapq.heappush(max_heap, (-L, -P))
        heapq.heappush(min_heap, (L, P))
        problem_dict[P] = L

    elif command[0] == 'solved':
        P = int(command[1])
        if P in problem_dict:
            del problem_dict[P]  # 딕셔너리에서 문제 번호 제거

    elif command[0] == 'recommend':
        x = int(command[1])
        if x == 1:
            # 가장 어려운 문제 찾기
            while -max_heap[0][1] not in problem_dict or problem_dict[-max_heap[0][1]] != -max_heap[0][0]:
                heapq.heappop(max_heap)  # 유효하지 않은 문제 제거
            print(-max_heap[0][1])  # 문제 번호 출력
        elif x == -1:
            # 가장 쉬운 문제 찾기
            while min_heap[0][1] not in problem_dict or problem_dict[min_heap[0][1]] != min_heap[0][0]:
                heapq.heappop(min_heap)  # 유효하지 않은 문제 제거
            print(min_heap[0][1])  # 문제 번호 출력
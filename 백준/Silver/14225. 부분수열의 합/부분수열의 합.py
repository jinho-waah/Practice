import sys
from collections import defaultdict
input = sys.stdin.readline

# 입력
N = int(input().strip())
S = list(map(int, input().split()))

# N일때 더하기로 나올 수 있는 숫자의 개수 2^N - 1, 그리고 그 숫자 자체의 수 N개
# 경우의 수는 최소 2^N 개 혹은 2^N + N - 1
# 즉 전부 구할 수 없음
# 여기서 문제를 풀때 모든 경우의 수를 구할 필요가 있냐 할때 딱히 아닌거 같음
# 그리디 알고리즘을 이용해서 풀면 좋을듯
# 먼저 sorting을 하고
S.sort()
# answwer = 1 이라고 잡음
answer = 1

for n in S:
    if n > answer:
        break
    answer += n

print(answer)

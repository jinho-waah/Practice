import heapq
import sys

input = sys.stdin.readline

def is_consistent(phone_numbers):
    # 전화번호 목록 정렬
    phone_numbers.sort()

    # 인접한 두 번호를 비교하여 접두어 관계가 있는지 확인
    for i in range(len(phone_numbers) - 1):
        # 현재 번호가 다음 번호의 접두어인지 확인
        if phone_numbers[i + 1].startswith(phone_numbers[i]):
            return "NO"
    return "YES"

t = int(input().strip())

results = []
for _ in range(t):
    n = int(input().strip())
    phone_numbers = [input().strip() for _ in range(n)]
    results.append(is_consistent(phone_numbers))

for result in results:
    print(result)
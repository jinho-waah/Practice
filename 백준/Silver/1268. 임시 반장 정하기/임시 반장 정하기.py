import sys
from collections import defaultdict, deque
from statistics import mean
input = sys.stdin.readline
sys.setrecursionlimit(2000)

# 입력 처리
N = int(input().strip())
class_number = [list(map(int, input().split())) for _ in range(N)]

# 학생별 같은 반 학생 수를 저장할 리스트
same_class_count = [0] * N

# 학생별 학년-반 비교
for i in range(N):
    for j in range(i + 1, N):
        # 학생 i와 학생 j가 같은 반이었던 적이 있는지 확인
        if any(class_number[i][k] == class_number[j][k] for k in range(5)):
            # 같은 반이었던 적이 있다면 서로 카운트 증가
            same_class_count[i] += 1
            same_class_count[j] += 1

# 최대 같은 반 학생 수를 가진 학생 찾기
max_count = max(same_class_count)
# 가장 먼저 찾은 학생의 번호 출력 (인덱스가 0부터 시작하므로 1을 더함)
print(same_class_count.index(max_count) + 1)
import sys
from collections import defaultdict, deque
input = sys.stdin.readline
sys.setrecursionlimit(2000)

# 입력 처리
# M, N, H = map(int, input().split())
gpa_dict = {
    "A+": 4.5,
    "A0": 4.0,
    "B+": 3.5,
    "B0": 3.0,
    "C+": 2.5,
    "C0": 2.0,
    "D+": 1.5,
    "D0": 1.0,
    "F": 0
}

total_credits = 0.0  # 전체 학점의 합
total_gpa = 0.0   # (학점 * 평점)의 합

for _ in range(20):
    _, credit, grade = input().split()
    credit = float(credit)

    # P 등급인 경우 계산에서 제외
    if grade == 'P':
        continue

    # 평점 계산
    point = gpa_dict[grade]
    total_credits += credit
    total_gpa += credit * point

# 전공평점 계산
if total_credits == 0:
    major_gpa = 0.0
else:
    major_gpa = total_gpa / total_credits

# 결과 출력 (소수점 6자리까지)
print(f"{major_gpa:.6f}")
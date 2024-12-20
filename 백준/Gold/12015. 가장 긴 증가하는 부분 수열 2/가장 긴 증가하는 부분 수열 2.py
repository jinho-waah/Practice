import sys
input = sys.stdin.readline
from bisect import bisect_left

def longest_increasing_subsequence(arr):
    lis = []  # 가상의 LIS 배열
    for num in arr:
        pos = bisect_left(lis, num)  # LIS 배열에서 num이 들어갈 위치 탐색
        if pos == len(lis):
            lis.append(num)  # num이 LIS 배열의 끝에 추가
        else:
            lis[pos] = num  # num으로 기존 값을 교체
    return len(lis)  # LIS 배열의 길이 반환

# 입력 처리
N = int(input().strip())
arr = list(map(int, input().split()))

# 결과 출력
print(longest_increasing_subsequence(arr))

import sys
input = sys.stdin.readline

# 입력 받기
n, m =  map(int,input().split())

# N!에서 k의 지수 개수를 구하는 방법은 k^i로 N을 계속 나눠주면서 나온 몫들의 합
def count_power_of_2(n):
    count = 0
    while n >= 2:
        n //= 2
        count += n
    return count

def count_power_of_5(n):
    count = 0
    while n >= 5:
        n //= 5
        count += n
    return count

result = min(count_power_of_2(n) - count_power_of_2(m) - count_power_of_2(n-m),
             count_power_of_5(n) - count_power_of_5(m) - count_power_of_5(n-m))
print(result)
# 이문제는 일반적으로 풀면 run time error가 무조건 남.
def fib(n):
    # if n == 1 or n == 2:
    #     # count1 += 1
    #     return 1
    # else:
    #     return fib(n - 1) + fib(n - 2)
    f = [0] * (n+1)
    f[1] = 1
    f[2] = 1
    for i in range(3, n+1):
        f[i] = f[i-1] + f[i-2]
    return f[n]
def fibonacci(n):
    # global count2
    # f = [0] * (n + 1)
    # f[1] = 1
    # f[2] = 1
    # for i in range(3, n + 1):
    #     # count2 += 1  # 코드2 호출 (덧셈이 발생할 때마다 증가)
    #     f[i] = f[i - 1] + f[i - 2]
    return n-2

# 입력 받기
n = int(input())

# 호출 횟수 초기화
# count1 = 0
# count2 = 0
# 재귀 방식으로 피보나치 수 구하기
print(fib(n), fibonacci(n))
# 동적 프로그래밍 방식으로 피보나치 수 구하기


# 결과 출력
# print(count1, count2)

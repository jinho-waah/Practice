import sys
input = sys.stdin.readline

def solve(n, p, q):
    memo = {0: 1}  # A(0) = 1

    def a(x):
        if x in memo:
            return memo[x]
        memo[x] = a(x // p) + a(x // q)
        return memo[x]

    return a(n)


# 입력 처리
N, P, Q = map(int, input().split())

# 결과 출력
print(solve(N, P, Q))
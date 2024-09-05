# 메모이제이션...
pd = [0] * 1001

def recursion(n):
    if pd[n]:
        return pd[n]
    elif n == 1:
        return 1

    count = 1

    for k in range(1, (n // 2) + 1):    # 규칙이 있음
        count += recursion(k)           # 수는  a1 + x1 + a1으로 표기가 되는데
                                        # 이는 즉 a1을 한 쪽으로만 생각하면 되고
    pd[n] = count                       # 2a1이라 생각하면 무조건 짝수임
    return count                        # 그리고 상승하는 정도를 보면 가우스 함수와 비슷하다
                                        # 그렇기에 몫을 구하는 수를 써서 누적시키면 된다.

T = int(input())
li = [int(input()) for _ in range(T)]

# print(li)
for i in li:
    print(recursion(i))

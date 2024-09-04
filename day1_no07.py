# 1 ~ n 까지 더한 수 = n(n+1)
# 풀이 방법: k만큼 연속 된 수를 더한 다는 것은 x + (x+1) + (x+2) .... (x+k-1)
# x를 묶으면 kx + (0+1+2...+k-1) = kx + (k-1)k/2 = N
# kx = N - (k-1)k/2 됨
# k,x,n 전부 자연수가 이므로 (k-1)/2 과 N/k 모두 자연수이어야 함
num = int(input())

count = 0
k = 1
while k * (k - 1) // 2 < num:
    if (num - (k * (k - 1)) // 2) % k == 0:
        count += 1
    k += 1
print(count)
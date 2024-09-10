import sys
input = sys.stdin.readline

N = int(input())

x = list(map(int, input().split()))
len_x = len(x)
k = set()

for i in range(len(x)-1):
    tmp = 0
    for j in range(i, len(x)):

if len(k) == 0:
    print(0)
else:
    print(" ".join(map(str, sorted(k))))


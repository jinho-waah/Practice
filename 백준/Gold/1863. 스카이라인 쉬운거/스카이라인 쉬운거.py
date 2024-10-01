import sys
input = sys.stdin.readline


n = int(input().strip())
sky_line = [list(map(int, input().split())) for _ in range(n)]

stack = []
count = 0

for x, y in sky_line:
    while stack and stack[-1][1] > y:
        stack.pop()
        count += 1

    if not stack or stack[-1][1] < y:
        stack.append((x, y))

while stack:
    cur = stack.pop()
    if cur[1] == 0: continue
    count += 1

print(count)
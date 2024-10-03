import sys
from collections import defaultdict, deque
from statistics import mean
input = sys.stdin.readline
sys.setrecursionlimit(2000)

# 입력 처리
N = int(input().strip())
data = [int(input().strip()) for _ in range(N)]
data_dict = defaultdict(int)
data.sort()
for d in data:
    data_dict[d] += 1

average_v = round(mean(data))
mid_v = data[len(data) // 2]

max_frequency = max(data_dict.values())
modes = [k for k, v in data_dict.items() if v == max_frequency]
modes.sort()

if len(modes) > 1:
    mode_v = modes[1]
else:
    mode_v = modes[0]

range_v = data[-1] - data[0]

print(average_v)
print(mid_v)
print(mode_v)
print(range_v)
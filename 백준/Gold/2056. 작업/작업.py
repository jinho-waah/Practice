import sys
from collections import deque

input = sys.stdin.readline
sys.setrecursionlimit(2000)

# 입력 처리
N = int(input().strip())  # 작업의 개수 N
tasks = [[] for _ in range(N + 1)]  # 각 작업의 후속 작업 리스트
indegree = [0] * (N + 1)  # 진입 차수
time = [0] * (N + 1)  # 각 작업의 소요 시간

# 작업 정보 입력 받기
for i in range(1, N + 1):
    line = list(map(int, input().split()))
    task_time = line[0]
    precedes = line[2:]
    time[i] = task_time
    # 후속 작업을 그래프에 저장
    for prereq in precedes:
        tasks[prereq].append(i)
        indegree[i] += 1

# 위상 정렬 수행
queue = deque()
dp = [0] * (N + 1)  # 각 작업이 끝나는 데 걸리는 최소 시간

# 진입 차수가 0인 작업을 큐에 삽입 (선행 작업이 없는 작업)
for i in range(1, N + 1):
    if indegree[i] == 0:
        queue.append(i)
        dp[i] = time[i]

# 위상 정렬을 통해 작업을 처리
while queue:
    current = queue.popleft()

    # 현재 작업의 후속 작업들을 순회
    for next_task in tasks[current]:
        # 다음 작업의 진입 차수를 감소
        indegree[next_task] -= 1
        # 다음 작업의 완료 시간 갱신 (최소 시간을 위해 최대값 적용)
        dp[next_task] = max(dp[next_task], dp[current] + time[next_task])
        # 진입 차수가 0이 된 작업을 큐에 삽입
        if indegree[next_task] == 0:
            queue.append(next_task)

# 모든 작업을 완료하는 데 걸리는 최소 시간 출력
print(max(dp))

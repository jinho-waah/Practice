import sys
# 입력 받기
input = sys.stdin.readline

N = int(input().strip())
events = []

for _ in range(N):
    in_time, out_time = input().strip().split()

    # 들어오는 시간 기록
    in_event =(in_time, 'in')
    # print(in_event)
    events.append(in_event)

    # 나가는 시간 기록
    out_event = (out_time, 'out')
    events.append(out_event)
    # print(events)
# 시간순으로 정렬하되, 시간이 같을 때는 'out' 이벤트를 먼저 처리하도록 함
events.sort(key=lambda x: (x[0], x[1] == 'in'))

# 현재 사용 중인 공간과 필요한 최대 공간을 계산
current_spaces = 0
max_spaces = 0

# print(events)
for event in events:
    if event[1] == 'in':
        current_spaces += 1
        max_spaces = max(max_spaces, current_spaces)
    else:
        current_spaces -= 1

# 결과 출력
print(max_spaces)

# 79652
# 464
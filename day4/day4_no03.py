week_num = int(input())

work_time_list = [4, 6, 4, 10]
work_time_dict = {}

for _ in range(week_num):
    for time in range(4):
        workers = input().replace('-', '').split()

        for worker in workers:
            if worker in work_time_dict:
                work_time_dict[worker] += work_time_list[time]
            else:
                work_time_dict[worker] = work_time_list[time]

# 만약 아무도 근무하지 않았으면 "Yes" 출력
if not work_time_dict:  # work_time_dict가 비었을 경우가 있네 ;;;
    print("Yes")
else:
    max_time = max(work_time_dict.values())
    min_time = min(work_time_dict.values())

    # 근무 시간 차이가 12시간 이하인지 확인
    if max_time - min_time <= 12:
        print("Yes")
    else:
        print("No")
# 31120
# 36
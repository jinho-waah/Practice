name_list = ["Inseo", "Junsuk", "Jungwoo", "Jinwoo", "Youngki"]

total_sum = [0] * 5

A_array = [list(map(int, input().split())) for _ in range(5)]
B_array = [list(map(int, input().split())) for _ in range(5)]

for x in range(5):  # x번 사람
    total = 0
    for y in range(5):  # y 번째 일
        work = sum(A_array[x][i] * B_array[i][y] for i in range(5))
        total += work
    total_sum[x] = total

min_work = min(total_sum)

for idx in range(4,-1,-1):  # Youngki, Jinwoo, Jungwoo, Junsuk, Inseo 순으로 탐색
    if total_sum[idx] == min_work:
        print(name_list[idx])
        break
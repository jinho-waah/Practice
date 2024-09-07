num = int(input())
# 학생들이 뽑은 번호표 / 0인덱스는 첫째 줄 학생의 번호표
student_num_list = list(map(int, input().split()))
# 학생들의 초기 순서 1 ~ num
student_queue = list(range(1,num+1))
new_queue = []

for i in range(num):
    new_queue.insert(i - student_num_list[i],i+1)

# 리스트를 공백으로 구분하면서 출력
print(*new_queue)

# 메모리 31120
# 시간 28
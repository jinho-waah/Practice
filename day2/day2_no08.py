starting_string = "어느 한 컴퓨터공학과 학생이 유명한 교수님을 찾아가 물었다."

student_string = '"재귀함수가 뭔가요?"'

professor_string_first_dialogue = '"잘 들어보게. 옛날옛날 한 산 꼭대기에 이세상 모든 지식을 통달한 선인이 있었어.'
professor_string_second_dialogue = '마을 사람들은 모두 그 선인에게 수많은 질문을 했고, 모두 지혜롭게 대답해 주었지.'
professor_string_third_dialogue = '그의 답은 대부분 옳았다고 하네. 그런데 어느 날, 그 선인에게 한 선비가 찾아와서 물었어."'

professor_string_middle = '"재귀함수는 자기 자신을 호출하는 함수라네"'
professor_string_last = "라고 답변하였지."
under_bar_string = "____"

def recursive(n, depth):
    print(under_bar_string * depth + student_string)
    # 종료 조건
    if depth == n:
        print(under_bar_string * depth + professor_string_middle)
    else:
        print(under_bar_string * depth + professor_string_first_dialogue)
        print(under_bar_string * depth + professor_string_second_dialogue)
        print(under_bar_string * depth + professor_string_third_dialogue)
        recursive(n, depth + 1)


    # 답변 출력
    print(under_bar_string * depth + professor_string_last)

# 입력 값 받아서 처리
num = int(input())  # 입력을 정수로 변환

# 시작 문구 출력
print(starting_string)
recursive(num, 0)

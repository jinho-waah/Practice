def find(expression, current_num, N):
    if current_num == N + 1:
        # 수식 평가를 위한 문자열을 만들고, 공백을 제거해서 숫자 연결 처리
        if eval(expression.replace(' ', '')) == 0:
            results.append(expression)
        return

    # 출력 그대로를 위해서 '+', '-', ' '의 순서가 중요함
    # 항상 공백을 우선적으로 recursive를 돌려야 함
    # 공백을 추가해서 숫자를 이어붙이는 경우
    find(expression + ' ' + str(current_num), current_num + 1, N)
    # +를 추가하는 경우
    find(expression + '+' + str(current_num), current_num + 1, N)
    # -를 추가하는 경우
    find(expression + '-' + str(current_num), current_num + 1, N)


T = int(input())
num_list = [int(input()) for _ in range(T)]

for i in range(len(num_list)):
    results = []
    N = num_list[i]
    find('1', 2, N)

    for result in results:
        print(result)
    # 출력 형태를 맞추기 위함
    if i != len(num_list)-1:
        print()



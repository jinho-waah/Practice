# def delete_parentheses(expression, length, counting):
#     # 제일 안에 있는 괄호 찾기
#     # ( 는 문자열 구조를 역순으로 바꾼후 index를 이용해 가장 먼저 찾고
#     # ) 는 index로 바로 찾으면 된다.
#     if counting > 0:
#         reverse_expression = expression[::-1]
#         left_index = length - reverse_expression.index('(') -1
#         right_index = expression.index(')')
#         new_expression = expression[:left_index] + expression[left_index+1:right_index]+expression[right_index+1:]
#         print(new_expression)
#         new_length = len(new_expression)
#         delete_parentheses(new_expression,new_length)
#     else:
#         return

#
# S = input()
# S_len = len(S)
# counting = S.count('(')
# delete_parentheses(S, S_len, counting)
#
# recursive 를 돌리는데 돌리는 순서가 중요함
# 괄호는 항상 제일 안에 있는 부분을 제거 해야하고
# 다시 원래 모양에서 두번째만 제거 하고
# 마지막 까지 제거해야한다.
# 그런다음 제거하는 갯수를 늘려야 한다.

# 조합을 생성하는 함수
def generate_combinations(arr, r):
    result = []

    def combine(start, chosen):
        if len(chosen) == r:
            result.append(chosen[:])
            return
        for i in range(start, len(arr)):
            chosen.append(arr[i])
            combine(i + 1, chosen)
            chosen.pop()

    combine(0, [])
    return result


# 괄호 쌍을 제거한 서로 다른 식을 생성하는 함수
def delete_parentheses(expression):
    stack = []
    pairs = []

    # 괄호 쌍의 위치를 찾아 저장
    for i, ch in enumerate(expression):
        if ch == '(':
            stack.append(i)
        elif ch == ')':
            start = stack.pop()
            pairs.append((start, i))

    result = set()

    # 모든 괄호 쌍을 조합적으로 제거
    for r in range(1, len(pairs) + 1):
        for comb in generate_combinations(pairs, r):
            temp_expr = list(expression)
            for start, end in comb:
                temp_expr[start] = ''
                temp_expr[end] = ''
            result.add(''.join(temp_expr))

    return sorted(list(result))


# 입력 받기
S = input()

# 괄호를 제거한 서로 다른 식들 생성
expressions = delete_parentheses(S)

# 사전순으로 출력
for expr in expressions:
    print(expr)

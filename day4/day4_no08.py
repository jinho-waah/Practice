


def is_balanced(s):
    stack = []

    for char in s:
        if char == '(' or char == '[':
            stack.append(char)
        elif char == ')':
            if not stack or stack[-1] != '(':
                return "no"
            stack.pop()
        elif char == ']':
            if not stack or stack[-1] != '[':
                return "no"
            stack.pop()
    # 모든 괄호가 맞으면 스택은 비어있어야 함
    if not stack:
        return "yes"
    else:
        return "no"


while True:
    # 입력 받기
    line = input().rstrip()
    if line == '.':  # 종료 조건
        break

    # 균형 여부 검사 후 출력
    print(is_balanced(line))

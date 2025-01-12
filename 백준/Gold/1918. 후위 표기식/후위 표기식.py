import sys
input = sys.stdin.readline

def infix_to_postfix(expression):
    # 연산자 우선순위 설정
    precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '(': 0}
    stack = []  # 연산자를 저장할 스택
    postfix = []  # 후위 표기식 결과를 저장할 리스트

    for char in expression:
        if char.isalpha():  # 피연산자(알파벳)일 경우 바로 결과에 추가
            postfix.append(char)
        elif char == '(':  # 여는 괄호는 스택에 추가
            stack.append(char)
        elif char == ')':  # 닫는 괄호일 경우
            while stack and stack[-1] != '(':
                postfix.append(stack.pop())  # 여는 괄호를 만날 때까지 팝
            stack.pop()  # 여는 괄호 제거
        else:  # 연산자인 경우
            while stack and precedence[stack[-1]] >= precedence[char]:
                postfix.append(stack.pop())  # 우선순위가 높은 연산자를 결과에 추가
            stack.append(char)  # 현재 연산자를 스택에 추가

    while stack:  # 스택에 남아 있는 모든 연산자를 결과에 추가
        postfix.append(stack.pop())

    return ''.join(postfix)

# 테스트 예제 실행
expression = input().strip()
result = infix_to_postfix(expression)
print(result)

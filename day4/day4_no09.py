def calculate_bracket_value(s):
    stack = []
    result = 0  # 최종 계산 결과
    temp = 1    # 중간 계산 값을 저장

    for i in range(len(s)):
        char = s[i]

        if char == '(':
            stack.append(char)
            temp *= 2  # '('는 2를 곱함
        elif char == '[':
            stack.append(char)
            temp *= 3  # '['는 3을 곱함
        elif char == ')':
            if not stack or stack[-1] != '(':
                return 0  # 올바르지 않은 괄호열
            if s[i-1] == '(':  # 바로 앞에 '('가 있으면 값을 더해줌
                result += temp
            stack.pop()  # '('와 매칭 완료
            temp //= 2  # 계산이 끝나면 2를 나눠줌
        elif char == ']':
            if not stack or stack[-1] != '[':
                return 0  # 올바르지 않은 괄호열
            if s[i-1] == '[':  # 바로 앞에 '['가 있으면 값을 더해줌
                result += temp
            stack.pop()  # '['와 매칭 완료
            temp //= 3  # 계산이 끝나면 3을 나눠줌

    # 스택에 남아있는 것이 없으면 올바른 괄호열
    if stack:
        return 0
    return result

# 입력 받기
s = input().strip()

# 결과 출력
print(calculate_bracket_value(s))

# 31120
# 36
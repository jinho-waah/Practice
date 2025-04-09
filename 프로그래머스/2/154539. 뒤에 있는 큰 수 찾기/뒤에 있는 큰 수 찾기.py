def solution(numbers):
    num_len = len(numbers)
    answer = [-1] * num_len
    stack = []
    for i in range(num_len-1, -1, -1):
        while stack and numbers[stack[-1]] <= numbers[i]:
            stack.pop()
        if stack:
            answer[i] = numbers[stack[-1]]
        stack.append(i)
    
    return answer
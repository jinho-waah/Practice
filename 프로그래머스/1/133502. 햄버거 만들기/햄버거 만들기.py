def solution(ingredient):
    answer = 0
#     1: 빵, 2: 야채, 3:고기
    stack = []
    
    for i in ingredient:
        if stack[-3:] == [1,2,3] and i == 1:
            stack.pop()
            stack.pop()
            stack.pop()
            answer += 1
        else:
            stack.append(i)
            
        
    return answer
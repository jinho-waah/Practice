def solution(s):
    answer = True
    li = []
    for i in s: 
        if li and li[-1] == '(' and i == ')':
            li.pop()
        else:
            li.append(i)
    if li != []:
        answer = False
    return answer
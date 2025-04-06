def solution(s):
    answer = ''
    make_upper = True  

    for char in s:
        if make_upper:
            answer += char.upper()
        else:
            answer += char.lower()
        
        make_upper = char == ' ' 
    return answer
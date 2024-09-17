def solution(s):
    answer = []
    char_dict = {}
    
    for i in range(len(s)):
        if s[i] not in char_dict:
            char_dict[s[i]] = i
            answer.append(-1)
        else:
            answer.append(i - char_dict[s[i]])
            char_dict[s[i]] = i
    return answer
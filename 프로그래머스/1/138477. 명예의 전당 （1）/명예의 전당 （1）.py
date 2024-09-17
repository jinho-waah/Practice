def solution(k, score):
    answer = []
    score_list = []
    
    for i in score:
        if len(score_list) < k:
            score_list.append(i)
            score_list.sort(reverse=True)
            answer.append(score_list[-1])
        else:
            score_list.append(i)
            
            score_list.sort(reverse=True)
            score_list.pop()
            answer.append(score_list[-1])
        
    return answer
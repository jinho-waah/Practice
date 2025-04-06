def solution(players, callings):
    answer = []
    rank_dict = {} # {등수 : 이름}
    name_dict = {} # {이름 : 등수}
    for i in range(len(players)):
        rank_dict[i+1] = players[i] 
        name_dict[players[i]] = i+1
        
    
    for name in callings: # 콜 받은 사람 이름
        name_dict[name] -= 1 # 콜 받은 사람 등수 올라가기
        lose_name = rank_dict[name_dict[name]] # 등수 내려간 사람 이름 구하기
        name_dict[lose_name] += 1 # 등수 내려간 사람 등수 적용
        rank_dict[name_dict[name]] = name # rank_dict에 등수 올라간 사람 적용
        rank_dict[name_dict[name] + 1] = lose_name
        
    for i in range(1, len(players) + 1):
        answer.append(rank_dict[i])
        
    return answer
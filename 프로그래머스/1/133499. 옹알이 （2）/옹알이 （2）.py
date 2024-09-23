def solution(babbling):
    answer = 0
    babbling_list = ["aya", "ye", "woo", "ma"]
    
    for word in babbling:
        prev_sound = ""
        flag = True
        i = 0
        while i < len(word):
            match_found = False
            for sound in babbling_list:
                # 현재 위치에서 발음이 맞으면 처리
                if word[i:i+len(sound)] == sound and sound != prev_sound:
                    i += len(sound)
                    prev_sound = sound
                    match_found = True
                    break
            
            if not match_found:
                flag = False
                break
        
        if flag:
            answer += 1 
            
            
    
    return answer
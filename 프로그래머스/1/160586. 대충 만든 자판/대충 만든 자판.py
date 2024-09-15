from collections import defaultdict

def solution(keymap, targets):
    answer = []
    key_dict = defaultdict(lambda: float('inf'))  # 초기값을 매우 큰 수로 설정
    
    # 각 문자가 눌리기 위해 필요한 최소 횟수 계산
    for key in keymap:
        for i in range(len(key)):
            # 현재 문자에 대해 최소 눌러야 하는 횟수를 갱신
            key_dict[key[i]] = min(key_dict[key[i]], i + 1)
    
    # 각 target에 대해 최소 키 누르기 횟수를 계산
    for target in targets:
        tmp = 0
        for t in target:
            if t in key_dict and key_dict[t] != float('inf'):
                tmp += key_dict[t]
            else:
                tmp = -1
                break  # 찾을 수 없는 문자가 있으면 바로 -1로 처리
        
        answer.append(tmp)
    
    return answer

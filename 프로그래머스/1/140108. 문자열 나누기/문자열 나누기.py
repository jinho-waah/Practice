def solution(s):
    answer = 0
    i = 0
    
    while i < len(s):
        x = s[i]  # 첫 글자
        same_count = 1  # 첫 글자 등장 횟수
        diff_count = 0  # 첫 글자가 아닌 다른 글자 등장 횟수
        
        # x와 x가 아닌 글자의 등장 횟수가 같아질 때까지 계속 확인
        for j in range(i + 1, len(s)):
            if s[j] == x:
                same_count += 1
            else:
                diff_count += 1
            
            if same_count == diff_count:
                i = j + 1  # 분리된 부분 다음 문자부터 시작
                break
        else:
            # 두 카운트가 같아지지 않으면 남은 문자열을 한 번에 분리
            i = len(s)
        
        # 새로운 부분 문자열이 만들어졌으므로 answer을 증가
        answer += 1
    
    return answer

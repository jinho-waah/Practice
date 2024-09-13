from datetime import datetime

def solution(today, terms, privacies):
    answer = []
    today_date = datetime.strptime(today, '%Y.%m.%d')

    # terms 딕셔너리 생성 (약관 종류별 유효기간)
    terms_dict = {e.split()[0]: int(e.split()[1]) for e in terms}

    # privacies 처리
    for i, privacy in enumerate(privacies):
        privacy_date_str, term_type = privacy.split()
        privacy_date = datetime.strptime(privacy_date_str, '%Y.%m.%d')
        
        # 약관에 따른 유효기간 계산 (월 단위로 더함)
        term_duration = terms_dict[term_type]
        year = privacy_date.year
        month = privacy_date.month + term_duration
        day = privacy_date.day  # 수집일자의 day를 그대로 유지
        
        # 월이 12를 넘으면 연도를 증가시킴
        while month > 12:
            month -= 12
            year += 1
        
        # 정확한 만료일은 수집일자의 day와 동일하게 설정
        expiration_date = datetime(year, month, day)

        # 오늘 날짜와 비교하여 유효기간이 지났는지 확인
        if today_date >= expiration_date:
            answer.append(i + 1)  # 개인정보 번호는 1부터 시작이므로 index + 1
    
    return answer

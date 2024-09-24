from collections import defaultdict

def solution(id_list, report, k):
    # 1. 중복 신고 제거
    report = set(report)
    
    # 2. 신고 당한 횟수를 저장할 딕셔너리
    report_count = defaultdict(int)
    
    # 3. 각 유저가 신고한 유저 리스트를 저장할 딕셔너리
    user_reports = defaultdict(set)
    
    # 4. 신고 기록 처리
    for r in report:
        user, reported = r.split()
        user_reports[user].add(reported)  # user가 신고한 유저 저장
        report_count[reported] += 1       # reported 유저가 신고당한 횟수 증가
    
    # 5. 정지된 유저 리스트 만들기
    suspended_users = {user for user, count in report_count.items() if count >= k}
    
    # 6. 각 유저가 받은 결과 메일 수 계산
    answer = []
    for user in id_list:
        # user가 신고한 유저 중에서 정지된 유저 수를 카운트
        mail_count = len(user_reports[user] & suspended_users)
        answer.append(mail_count)
    
    return answer

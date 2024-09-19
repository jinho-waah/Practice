def solution(k, m, score):
    answer = 0
    score.sort(reverse=True)  # 사과 점수를 내림차순으로 정렬
    for i in range(0, len(score), m):
        if len(score[i:i+m]) == m:  # 사과가 m개 있는 상자만 고려
            answer += min(score[i:i+m]) * m  # 최저 점수 * m (상자 내 사과 개수)
    return answer
def solution(n, m, section):
    answer = 0  # 페인트칠 횟수
    last_painted = 0  # 마지막으로 페인트칠을 끝낸 구역

    for sec in section:
        # 현재 구역이 마지막으로 페인트칠한 구역을 넘어서면 새로운 롤러로 칠함
        if sec > last_painted:
            answer += 1  # 페인트칠 횟수 증가
            last_painted = sec + m - 1  # 현재 구역부터 롤러로 m미터까지 칠함

    return answer
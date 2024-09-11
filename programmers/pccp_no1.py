def solution(bandage, health, attacks):
    t, x, y = bandage  # 붕대 감기 정보: t초 동안 x만큼 회복, t초 연속 성공 시 y 추가 회복
    max_health = health  # 최대 체력
    current_health = health  # 현재 체력
    attack_times = {time: damage for time, damage in attacks}  # 공격 시간을 딕셔너리로 변환

    time = 0  # 현재 시간
    success_time = 0  # 연속으로 기술이 성공한 시간

    while current_health > 0:
        time += 1

        # 몬스터의 공격이 있는지 확인
        if time in attack_times:
            current_health -= attack_times[time]  # 공격으로 체력 감소
            success_time = 0  # 기술이 취소됨, 연속 성공 시간 초기화
            continue  # 공격을 받은 시간이므로 체력을 회복하지 않음

        # 붕대 감기를 통해 체력 회복
        current_health += x  # 매초 x만큼 체력 회복
        current_health = min(current_health, max_health)  # 최대 체력을 넘지 않도록 함
        success_time += 1  # 성공 시간 증가

        # t초 연속으로 성공하면 추가 회복
        if success_time == t:
            current_health += y  # 추가 회복
            current_health = min(current_health, max_health)  # 최대 체력을 넘지 않도록 함
            success_time = 0  # 연속 성공 시간 초기화

        # 공격이 끝난 경우
        if time > max(attack_times.keys()):
            return current_health  # 모든 공격이 끝난

    return -1
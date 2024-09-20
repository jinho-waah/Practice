def solution(food):
    left_side = []

    # 각 음식을 두 선수에게 공정하게 나누어주기 위한 배치
    for i in range(1, len(food)):
        # i번 음식을 두 선수가 동일하게 먹을 수 있는 개수만큼 추가
        left_side.append(str(i) * (food[i] // 2))

    # 왼쪽 음식 배치, 물(0) 배치, 오른쪽 음식(왼쪽 음식의 역순) 배치
    result = ''.join(left_side) + '0' + ''.join(left_side[::-1])
    return result

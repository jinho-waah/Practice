# 가장 많이 받은 선물

from collections import defaultdict
def solution(friends, gifts):
    # 각 친구가 받은 선물, 준 선물을 기록할 딕셔너리
    gave = defaultdict(int)  # 각 친구가 준 선물 수
    received = defaultdict(int)  # 각 친구가 받은 선물 수
    interactions = defaultdict(lambda: defaultdict(int))  # A가 B에게 준 선물 횟수

    # 선물 주고받기 기록 처리
    for gift in gifts:
        giver, receiver = gift.split()
        gave[giver] += 1
        received[receiver] += 1
        interactions[giver][receiver] += 1

    # 다음 달에 받을 선물 수를 기록할 딕셔너리
    next_gifts = defaultdict(int)

    print(gave)
    print(received)
    print(interactions)
    # 각 친구 쌍에 대해 다음 달에 받을 선물 계산
    for friend1 in friends:
        for friend2 in friends:
            if friend1 == friend2:
                continue  # 자기 자신과는 비교하지 않음

            # friend1이 friend2에게 준 선물 수와 받은 선물 수
            gave_to_friend2 = interactions[friend1][friend2]
            received_from_friend2 = interactions[friend2][friend1]

            if gave_to_friend2 > received_from_friend2:
                next_gifts[friend1] += 1  # friend1이 더 많이 줬으므로 friend2가 선물 하나 줌
            elif gave_to_friend2 < received_from_friend2:
                next_gifts[friend2] += 1  # friend2가 더 많이 줬으므로 friend1이 선물 하나 줌
            else:  # 주고받은 선물이 같다면
                # 선물 지수 비교: 선물 지수는 준 선물 - 받은 선물
                gift_index1 = gave[friend1] - received[friend1]
                gift_index2 = gave[friend2] - received[friend2]

                if gift_index1 > gift_index2:
                    next_gifts[friend1] += 1  # friend1의 선물 지수가 높으면 friend2가 선물 하나 줌
                elif gift_index1 < gift_index2:
                    next_gifts[friend2] += 1  # friend2의 선물 지수가 높으면 friend1이 선물 하나 줌
                # 같으면 아무도 선물 주고받지 않음

    # 가장 많이 선물 받을 친구가 받을 선물 수 찾기
    max_gifts = max(next_gifts.values(), default=0)

    return max_gifts / 2

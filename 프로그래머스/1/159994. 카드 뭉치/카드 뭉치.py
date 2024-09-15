def solution(cards1, cards2, goal):
    for word in goal:
        if cards1 and word == cards1[0]:
            cards1.pop(0)  # cards1의 첫 번째 단어를 사용
        elif cards2 and word == cards2[0]:
            cards2.pop(0)  # cards2의 첫 번째 단어를 사용
        else:
            return "No"  # 해당 단어가 cards1과 cards2에서 사용될 수 없으면 "No" 반환
    return "Yes"
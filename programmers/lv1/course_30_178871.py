# 달리기 경주
# 범위가 너무 커서 리스트를 사용하면 시간 초과
# 그러므로 해시를 쓰는게 좋음

def solution(players, callings):
    answer = []
    player_dict = {players[i]: i for i in range(len(players))}
    rank_dict = {i: players[i] for i in range(len(players))}

    for called in callings:
        rank = player_dict[called]
        slower_racer = rank_dict[rank - 1]
        player_dict[called] -= 1
        player_dict[slower_racer] += 1
        rank_dict[rank] = slower_racer
        rank_dict[rank - 1] = called

    answer = list(rank_dict.values())
    return answer
import sys

input = sys.stdin.readline


N = int(input().strip())

star_link = [list(map(int, input().split())) for _ in range(N)]

min_diff = float('inf')
visited = [False] * N

# 능력치 계산 함수
def calculate_ability(team):
    ability = 0
    for i in range(len(team)):
        for j in range(i + 1, len(team)):
            ability += star_link[team[i]][team[j]]
            ability += star_link[team[j]][team[i]]
    return ability


# 백트래킹 함수
def backtrack(index, count):
    global min_diff

    # N/2명을 선택하면 팀을 나눔
    if count == N // 2:
        start_team = []
        link_team = []

        for i in range(N):
            if visited[i]:
                start_team.append(i)
            else:
                link_team.append(i)

        # 두 팀의 능력치를 계산하고 차이를 구함
        start_ability = calculate_ability(start_team)
        link_ability = calculate_ability(link_team)
        diff = abs(start_ability - link_ability)
        min_diff = min(min_diff, diff)

        return

    # 백트래킹을 통한 팀 구성
    for i in range(index, N):
        if not visited[i]:
            visited[i] = True
            backtrack(i + 1, count + 1)
            visited[i] = False


# 백트래킹 시작
backtrack(0, 0)

# 결과 출력
print(min_diff)
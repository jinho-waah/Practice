# 먼저 하노이 탑에 대해서 조금 알고 있어야 한다.
# 작은 원판 위에 큰 원판은 올라 갈 수 없다.
# 옮기는 횟수는 2**n-1 회다.
# 하노이의 탑을 옮기기 위해서는 3가지 변수가 필요하다
# 출발지, 도착지, 경유지가 필요하다
# 간단한 예로
# 2층의 탑을 옮기기 위해서는 총 3번을 옮겨야 한느데

# i)
#  ㅁㅁㅁ
# ㅁㅁㅁㅁㅁ

# ii)
#
# ㅁㅁㅁㅁㅁ       ㅁㅁㅁ

# iii)
#
#               ㅁㅁㅁ         ㅁㅁㅁㅁㅁ

# iv)
#                              ㅁㅁㅁ
#                             ㅁㅁㅁㅁㅁ

# 이렇게 중간 공간을 꼭 거쳐야 한다.

def hanoi(n, departure, destination, via):  #3개의 위치
    if n == 1:
        print(departure, destination)       # 마지막 도착
        return
    hanoi(n-1, departure, via, destination)  # N-1개의 원판을 중간 장대로 옮김
    print(departure, destination)            # 가장 큰 원판을 목적지로 옮김
    hanoi(n-1, via, destination, departure)  # 중간 장대에 있던 N-1개의 원판을 목적지로 옮김

N = int(input())
print(2 ** N -1)

hanoi(N, 1,3,2)
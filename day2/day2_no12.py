

def hanoi(n, departure, destination, via):  #3개의 위치
    if n == 1:
        print(departure, destination)       # 마지막 도착
        return
    hanoi(n-1, departure, via, destination)  # N-1개의 원판을 중간 장대로 옮김
    print(departure, destination)            # 가장 큰 원판을 목적지로 옮김
    hanoi(n-1, via, destination, departure)  # 중간 장대에 있던 N-1개의 원판을 목적지로 옮김

N = int(input())
print(2 ** N -1)
if N <= 20:
    hanoi(N, 1,3,2)
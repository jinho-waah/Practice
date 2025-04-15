'''
dp

f(1) = f(2) = 1

a b c d   => n-1
e f g h   => n-2
'''


def solution(land):
    for i in range(1, len(land)):
        for j in range(4):
            land[i][j] += max(land[i-1][k] for k in range(4) if k != j)
    answer = 0
    
    return max(land[-1])
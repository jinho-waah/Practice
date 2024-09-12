# 격자 같은 색 찾기

def solution(board, h, w):
    answer = 0
    n = len(board)
    dh = [0, 1, -1, 0]
    dw = [1, 0, 0, -1]

    for i in range(4):
        h_check, w_check = h + dh[i], w + dw[i]
        if n > h_check >= 0 and n > w_check >= 0:
            if board[h][w] == board[h_check][w_check]:
                answer += 1

    return answer

dp = {}

def dfs(x, y, mask):
    if (x, y, mask) in dp:
        return dp[(x, y, mask)]
    
    dp[(x, y, mask)] = 1
    for dx, dy in [(0,1),(1,0),(0,-1),(-1,0)]:
        nx, ny = x+dx, y+dy
        if 0 <= nx < r and 0 <= ny < c:
            alpha_idx = ord(board[nx][ny]) - ord('A')
            nxt_bit = (1 << alpha_idx)
            if not (mask & nxt_bit):
                dp[(x, y, mask)] = max(dp[(x, y, mask)],
                                       1 + dfs(nx, ny, mask | nxt_bit))
    return dp[(x, y, mask)]

r, c = map(int, input().split())
board = [input().rstrip() for _ in range(r)]

start_char = board[0][0]
start_mask = 1 << (ord(start_char) - ord('A'))

ans = dfs(0, 0, start_mask)
print(ans)
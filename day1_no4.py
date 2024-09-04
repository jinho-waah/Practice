row, col = map(int, input().split())
bungeo = [input() for _ in range(row)]

for r in bungeo:
    # 입력 받은 값 역순으로 배열
    print(r[::-1])
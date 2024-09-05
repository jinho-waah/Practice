def cantor(start, length, arr):
    if length == 1:
        return
    third = length // 3
    # 가운데 부분을 공백으로 변경
    for i in range(start + third, start + 2 * third):
        arr[i] = ' '
    # 왼쪽 부분 재귀 호출
    cantor(start, third, arr)
    # 오른쪽 부분 재귀 호출
    cantor(start + 2 * third, third, arr)


# 입력 받기
while True:
    try:
        N = int(input())

        if N == 0:
            print('-')
        else:
            length = 3 ** N
            arr = ['-'] * length
            cantor(0, length, arr)
            print(''.join(arr))
    except:
        break

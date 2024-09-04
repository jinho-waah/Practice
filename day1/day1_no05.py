# 참외의 개수 입력
K = int(input())

# 육각형의 변과 길이 입력
sides = [list(map(int, input().split())) for _ in range(6)]

# 가장 큰 가로 길이와 세로 길이를 찾기 위한 변수 초기화
max_width = 0
max_height = 0

# 가로와 세로 최대값 및 최소값 찾기
# 여기서 규칙. 어떠한 경우라도 max_width에 해당하는 인덱스 값에 3을 더하면 small_height를 구할 수 있고
# max_height에 3을 더하면 small_width를 구할 수 있다.
for i in range(6):
    direction, length = sides[i]
    if direction == 1 or direction == 2:  # 동, 서 방향
        if length > max_width:
            max_width = length
            small_height = sides[(i + 3) % 6][1]

    else:  # 남, 북 방향
        if length > max_height:
            max_height = length
            small_width = sides[(i + 3) % 6][1]



# 최종 넓이 계산
result = (max_width * max_height - small_width * small_height) * K
print(result)

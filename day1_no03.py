def print_star(num):
    # 상단 부분 (1번째 줄부터 N번째 줄까지)
    for i in range(1, num + 1, 1):
        left_stars = '*' * i
        spaces = ' ' * (2 * (num - i))
        right_stars = '*' * i
        print(left_stars + spaces + right_stars)

    # 하단 부분 (N+1번째 줄부터 2*N-1번째 줄까지)
    for i in range(num - 1, 0, -1):
        left_stars = '*' * i
        spaces = ' ' * (2 * (num - i))
        right_stars = '*' * i
        print(left_stars + spaces + right_stars)



num = int(input())
print_star(num)
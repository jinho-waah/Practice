num = int(input())

#모양은 n X n 정사각형이다
# 이 문제는 홀수 줄과 짝수 줄을 나눠서 규칙을 찾고
# 그 규칙을 이용해 리스트로 별을 수정하면 됨
# 중간 줄의 개수는 2n-1개로 정해져있으므로
# 모양의 상단과 하단을 나눠서 실행
# 문제의 의도는 이게 아닌거 같은 느낌적인 느낌..
start_length = 1 + (num-1) * 4
odd_star_to_list = ["*"] * start_length
even_star_to_list = ["*"] + [" "] * (start_length -2) + ["*"]


for i in range(2 * num -2):
    if i % 2 == 0:
        if i != 0:
            odd_star_to_list[i-1] = ' '
            odd_star_to_list[start_length - i] = ' '
        print(''.join(odd_star_to_list))
    else:
        if i != 1:
            even_star_to_list[i-1] = '*'
            even_star_to_list[start_length-i] = '*'
        print(''.join(even_star_to_list))


#중간의 길이는 4n-3, 별의 개수는 2n-1
middle_start = "* " * (2 * num -2) + "*"
print(middle_start)


for i in range(2 * num -2, 0, -1):
    # print(i)
    if i % 2 == 0:
        if i != (2 * num -2):
            even_star_to_list[i] = ' '
            even_star_to_list[start_length-i-1] = ' '
        print(''.join(even_star_to_list))

    else:
        odd_star_to_list[i] = '*'
        odd_star_to_list[start_length-i-1] = '*'
        print(''.join(odd_star_to_list))


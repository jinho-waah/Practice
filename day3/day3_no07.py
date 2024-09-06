
def make_reverse(S):
    result = []
    word = []
    inside_flag = False  # 태그 안에 있는지 여부

    for char in S:
        if char == '<':
            # 단어가 있으면 먼저 뒤집고 추가
            if word:
                result.append(''.join(reversed(word)))
                word = []
            # 태그의 시작
            inside_flag = True
            result.append(char)
        elif char == '>':
            # 태그의 끝
            inside_flag = False
            result.append(char)
        elif inside_flag:
            # 태그 안에서는 그대로 추가
            result.append(char)
        elif char == ' ':
            # 단어가 있으면 뒤집어서 추가
            if word:
                result.append(''.join(reversed(word)))
                word = []
            # 공백은 그대로 추가
            result.append(char)
        else:
            # 태그 밖에서는 단어를 계속 이어서 작성
            word.append(char)

    # 마지막 단어 처리
    if word:
        result.append(''.join(reversed(word)))

    return ''.join(result)

# 입력 받기
S = input()

# 결과 출력
print(make_reverse(S))


# memory 32684
# time 44
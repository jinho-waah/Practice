from collections import Counter

def solution(X, Y):
    answer = ''
    
    count_X = Counter(X)
    count_Y = Counter(Y)
    
    common_digits = []
    for digit in range(10):  # 0부터 9까지 숫자 확인
        if str(digit) in count_X and str(digit) in count_Y:
            common_count = min(count_X[str(digit)], count_Y[str(digit)])
            common_digits.extend([str(digit)] * common_count)
    
    # 공통된 숫자가 없다면 -1 반환
    if not common_digits:
        return "-1"
    
    # 큰 수를 만들기 위해 숫자를 내림차순으로 정렬
    common_digits.sort(reverse=True)
    
    # 결과가 0으로만 구성되어 있다면 0 반환
    if common_digits[0] == '0':
        return "0"
    
    # 문자열로 반환
    return ''.join(common_digits)
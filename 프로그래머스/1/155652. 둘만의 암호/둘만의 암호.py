def solution(s, skip, index):
    # skip 문자열을 집합으로 변환하여 빠르게 확인할 수 있도록 함
    skip_set = set(skip)
    result = []
    
    for char in s:
        count = 0
        current_char = char
        
        # index만큼 알파벳을 뒤로 이동 (skip을 건너뛰면서)
        while count < index:
            current_char = chr(((ord(current_char) - ord('a') + 1) % 26) + ord('a'))
            if current_char not in skip_set:
                count += 1
        
        result.append(current_char)
    
    return ''.join(result)
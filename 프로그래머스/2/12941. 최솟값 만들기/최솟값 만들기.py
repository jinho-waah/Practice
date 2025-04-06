def solution(A,B):
    answer = 0
    sorted_a = sorted(A)
    sorted_b = sorted(B)
    
    for i in range(len(A)):
        answer += sorted_a[i] * sorted_b[-(i+1)]

    return answer

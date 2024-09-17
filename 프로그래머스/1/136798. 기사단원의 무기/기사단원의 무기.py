from math import sqrt

def solution(number, limit, power):
    answer = 0
    
    def count_divisor(num):
        count = 0
        for k in range(1, int(sqrt(num)) + 1):
            if num % k == 0:
                count += 1  # k는 약수
                if k != num // k:
                    count += 1  # num // k는 k와 다른 약수
                
        return(count)
        
    for n in range(1, number+1):
        count = count_divisor(n)
        if count > limit:
            answer += power
        else:
            answer += count
    return answer
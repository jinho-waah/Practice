def solution(n):
    answer = 0
    arr = [0,1]
    
    for i in range(1, n):
        arr.append(arr[i] + arr[i-1])
        
    answer = arr[n] % 1234567
    
    return answer
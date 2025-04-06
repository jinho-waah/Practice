def solution(s):
    answer = ''
    arr1 = s.split(' ')
    arr2 = [int(i) for i in arr1]
    
    answer =f'{min(arr2)} {max(arr2)}' 
        
    return answer
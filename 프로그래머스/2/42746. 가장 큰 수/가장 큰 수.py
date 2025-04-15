
'''

[8, 89, 1] > 89가 첫번째
[9, 98, 1] > 9가 첫번째
9901

NlogN + ?
3       333
30      303030
33      333333
34      343434
'''

def solution(numbers):
    answer = ''
    '''
    숫자로 정렬하는 것이 아니라
    문자열로 정렬하면 좋을 것
    '''
    str_list = list(map(str, numbers))
    str_list.sort(key=lambda x: x*3, reverse=True)
    
    if str_list[0] == '0':
        return '0'
    return ''.join(str_list)
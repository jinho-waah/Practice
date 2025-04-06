def solution(n):
    answer = n + 1
#     binary = bin(n)[2:]
#     length = len(binary)
#     if binary.count('0') == 0:
#         s1 = binary[:1] + '0' + binary[1:]
#         answer = int(binary[:1] + '0' + binary[1:],2)
#     else:
#         for i in range(1, length):
#             if binary[i] == '0':
    while bin(n).count('1') != bin(answer).count('1'):
        answer += 1
    return answer
# string = input()
#
# part_list = []
# for i in range(len(string)):
#     for j in range(i + 1, len(string) + 1):
#         if string[i:j] not in part_list:
#             part_list.append(string[i:j])
#
# print(len(part_list))
#
# 위 코드는 복잡도가 O(n^3)
# 이유는 이중 for문에 if문에서 not in을 검색하면서 *n 의 복잡도를 갖게 된다.
# 그러므로 set()을 쓰면 효율적이다.
# 입력 받기

S = input()

# 부분 문자열을 저장할 집합
part_list = set()

# 부분 문자열 생성 (모든 시작점과 끝점 조합에 대해)
for i in range(len(S)):
    for j in range(i + 1, len(S) + 1):
        part_list.add(S[i:j])

# 서로 다른 부분 문자열의 개수 출력
print(len(part_list))

# memory 240712
# time 476

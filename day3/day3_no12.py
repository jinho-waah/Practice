# 실제 구현은 어렵지 않음
# 하지만 밑의 그리디 알고리즘을 적용하지 않으면 시간 초과 혹은 런타임에러가 뜨게 됨

S = input()
stack = []
ppap = ["P", "P", "A", "P"]
len_S = len(S)
for i in range(len_S):          # 여기서부터가 그리디 알고리즘의 포인트
    stack.append(S[i])
    if stack[-4:] == ppap:      # 그리디 ppap가 바로 포착 되는 순간
        for _ in range(4):
            stack.pop()         # ppap를 바로 pop시키면서
        stack.append("P")       # p를 입력하게 된다.
if stack == ppap or stack == ["P"]:
    print("PPAP")
else:
    print("NP")

    # 그리디 알고리즘은 근시안적인 방식이며 최적값을 찾기는 힘들다
    # 트리 형태로 봤을때 모든 노드를 검사해봐야 최적값을 찾지만
    # 그리디 알고리즘은 한 노드를 내려갈때마다 그때의 최적의 선택을 하고
    # 그 외의 선택을 철저히 무시하기 때문에
    # 단기적인 성과를 내기 좋은 알고리즘이다
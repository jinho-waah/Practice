def solution(prices):
    answer = [0] * len(prices)
    stack = []

    for i in range(len(prices)):
        # 현재 가격이 이전 가격보다 떨어졌을 경우
        while stack and prices[i] < prices[stack[-1]]:
            top = stack.pop()
            answer[top] = i - top
        stack.append(i)

    # 아직 가격이 떨어지지 않은 인덱스 처리
    while stack:
        top = stack.pop()
        answer[top] = len(prices) - 1 - top

    return answer

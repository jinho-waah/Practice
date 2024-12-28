import sys
input = sys.stdin.readline

def min_clicks_to_channel(n, broken_buttons):
    broken = set(broken_buttons)
    min_clicks = abs(n - 100)  # 초기값: +, -만 사용하는 경우

    # 숫자 버튼으로 이동 가능한 경우 계산
    for target in range(1000000):  # 0부터 999,999까지 탐색
        target_str = str(target)
        if all(int(ch) not in broken for ch in target_str):  # 고장난 버튼 없이 입력 가능
            # 숫자 입력 횟수 + 현재 채널과의 차이
            min_clicks = min(min_clicks, len(target_str) + abs(n - target))

    return min_clicks

# 입력 처리
n = int(input().strip())
m = int(input().strip())
if m > 0:
    broken_buttons = list(map(int, input().split()))
else:
    broken_buttons = []

# 결과 계산 및 출력
print(min_clicks_to_channel(n, broken_buttons))

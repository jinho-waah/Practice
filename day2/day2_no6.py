def code1(n, count):
    count += 1  # 함수 호출 시마다 count 증가
    if n == 1 or n == 2:
        return 1
    else:
        return code1(n - 1, count) + code1(n - 2, count)

def code2(n, count):
    li = [0] * (n + 1)
    li[1] = 1
    li[2] = 1

    # 피보나치 수를 동적 프로그래밍으로 계산
    for i in range(3, n + 1):
        count += 1  # 덧셈 연산 시마다 count 증가
        li[i] = li[i - 1] + li[i - 2]

    # n번째 피보나치 수 반환
    return li[n]

if __name__ == "__main__":
    print("err1")
    num = int(input())
    print("err")
    count1 = 0  # code1의 호출 횟수 추적
    count2 = 0  # code2의 덧셈 연산 횟수 추적

    # 재귀 함수 호출
    code1(num, count1)

    # 동적 프로그래밍 함수 호출
    code2(num, count2)

    # 결과 출력
    print(count1, count2)

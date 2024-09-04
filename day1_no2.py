def verify():
    # 입력받은 문자열을 공백으로 분리하고 정수로 변환
    numbers = list(map(int, input().split()))
    # 만들어진 리스트를 for문을 이용하여 값 도출
    verification_number = sum(num ** 2 for num in numbers) % 10

    print(verification_number)

# 함수 실행
if __name__ == "__main__":
    verify()
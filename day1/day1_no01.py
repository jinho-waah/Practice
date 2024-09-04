def compare_numbers():
    # 입력받은 문자열을 공백으로 분리하고 정수로 변환
    A_str = input().strip()
    A_B = A_str.split()

    A = int(A_B[0])
    B = int(A_B[1])

    # 비교 연산 수행 및 결과 출력
    if A > B:
        print(">")
    elif A < B:
        print("<")
    else:
        print("==")


# 함수 실행
if __name__ == "__main__":
    compare_numbers()
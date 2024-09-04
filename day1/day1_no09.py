T = int(input())  # 테스트 케이스 수
# 각 테스트 케이스마다 분자와 분모를 입력받아 리스트로 저장
num_list = [list(map(int, input().split())) for _ in range(T)]

# 각 테스트 케이스마다 분자(i)와 분모(j)를 꺼내서 처리
for i, j in num_list:
    # 1. 정수 부분 계산 (분자 // 분모)
    integer_part = i // j  # i: 분자, j: 분모
    # 2. 나머지 계산 (나머지를 이용해 소수점 부분을 계산)
    remainder = i % j

    # 만약 나머지가 0이면, 순환 소수 없이 정수로 나누어 떨어짐
    if remainder == 0:
        print(f"{integer_part}.(0)")  # 소수점이 없음을 나타내기 위해 .(0) 출력

    else:
        # 3. 소수 부분 계산을 위해 리스트와 사전(딕셔너리) 준비
        decimal_part = []  # 소수점 이하의 각 자리를 저장할 리스트
        remainders = {}  # 나머지가 이전에 나왔는지 기록할 딕셔너리
        repeating_flag = -1  # 반복되는 소수의 시작 위치를 저장 (-1이면 반복 없음)
        idx = 0  # 소수 부분의 인덱스를 관리

    # 4. 소수 부분 계산
        while remainder != 0:
            # 현재 나머지가 이전에 나왔는지 확인 (즉, 순환이 시작되는지 확인)
            if remainder in remainders:
                repeating_flag = remainders[remainder]   # 순환 시작 위치 기록
                break  # 순환이 시작되면 반복문 종료

            # 현재 나머지의 위치를 기록 (나머지가 발생한 위치 기록)
            remainders[remainder] = idx

            # 나머지에 10을 곱하고 분모로 나누어 소수 부분을 계산
            remainder *= 10
            decimal_part.append(str(remainder // j))  # 소수 자리를 계산해 리스트에 추가
            remainder %= j  # 다시 나머지를 계산
            idx += 1  # 소수 부분의 자릿수 증가

        # 5. 소수 부분 출력
        # 반복되는 부분이 없는 경우
        if repeating_flag == -1:
            # 소수 부분을 전부 출력하고, 마지막에 (0)으로 표시
            print(f"{integer_part}."+"".join(decimal_part)+"(0)")

        else:
            # 반복되는 부분이 있는 경우
            # 반복되지 않는 부분과 반복되는 부분을 나누어 출력
            non_repeating = "".join(decimal_part[:repeating_flag])  # 반복되지 않는 부분
            repeating = "".join(decimal_part[repeating_flag:])  # 반복되는 부분
            print(f"{integer_part}.{non_repeating}({repeating})")  # 순환 부분을 괄호로 감싸서 출력

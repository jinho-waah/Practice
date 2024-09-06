phone_list = input().split()
T = input()

count = 0
for phone in phone_list:

    if phone.startswith(T) and phone != T:
        count += 1

# 결과 출력
print(count)

# memory 39164
# time 60
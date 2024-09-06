num1, num2 = input().split()

if num1[::-1] > num2[::-1]:
    print(num1[::-1])
else:
    print(num2[::-1])

# memory 31120
# time 32
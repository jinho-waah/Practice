N = int(input())
string_list = [input() for _ in range(N)]

result = 0

for ele in string_list:
    storage = []
    for i in ele:
        if len(storage) == 0:
            storage.append(i)
        elif storage[-1] == i:
            storage.pop(-1)
        else:
            storage.append(i)

    if len(storage) == 0:
        result += 1

print(result)

# 31744
# 116
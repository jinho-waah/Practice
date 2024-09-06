num = int(input())

extension_list = [input().split('.') for _ in range(num)]
counting_dict = {}
for i in extension_list:
    if i[1] in counting_dict:
        counting_dict[i[1]] += 1
    else:
        counting_dict[i[1]] = 1

sorted_dict = sorted(counting_dict.items())
for extension in sorted_dict:
    print(extension[0], extension[1])

# memory 51160
# time 1268
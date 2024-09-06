fruit_dict = {"STRAWBERRY":0, "BANANA":0, "LIME":0, "PLUM":0}

num = int(input())

set_list = [list(input().split()) for _ in range(num)]
flag = 0

for fruit, count in set_list:
    fruit_dict[fruit] += int(count)

for fruit in fruit_dict:
    if fruit_dict[fruit] == 5:
        flag = 1
        break
    else:
        flag = 0

if flag == 1:
    print("YES")
else:
    print("NO")


# memory 46236
# time 2456
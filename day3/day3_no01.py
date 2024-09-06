num = int(input())

string_list = [list(input().split()) for _ in range(num)]

for index, string in string_list:
    string_to_print = ""

    for l in string:
        string_to_print += l * int(index)
    print(string_to_print)

# memory 31120
# time 32
Q = int(input())

queries_list = [input() for _ in range(Q)]
query_dict = {}
result = 0

for query in queries_list:
    seller = query[2:].split()[0]
    if query[0] == "1":
        if seller in query_dict:
            query_dict[seller] += (query[2:].split()[2:])
        else:
            query_dict[seller] =  query[2:].split()[2:]

    else:
        if seller in query_dict:
            purchase_num = int(query[2:].split()[1])
            sorted_list = sorted(map(int, query_dict[seller]), reverse=True)
            if purchase_num >= len(sorted_list):
                result += sum(sorted_list)
                query_dict[seller] =[]
            else:
                result += sum(sorted_list[:purchase_num])
                query_dict[seller] = sorted_list[purchase_num:]

print(result)

# 45212
# 2684
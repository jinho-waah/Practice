num = int(input())

book_list = [input() for _ in range(num)]
book_dict = {}

for book in book_list:
    if book in book_dict:
        book_dict[book] += 1
    else:
        book_dict[book] = 1

sorted_books = sorted(book_dict.items(), key=lambda x: (-x[1], x[0]))
print(sorted_books[0][0])

# memory 31120
# time 32
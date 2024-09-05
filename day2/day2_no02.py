
num = int(input())
string_list = [input() for _ in range(num)]

count = 0
#두 함수는 문제 내용 그대로 구현
def recursion(s, l, r):
    global count
    count += 1
    if l >= r:
        print(f"1 {count}")
    elif s[l] != s[r]:
        print(f"0 {count}")
    else:
        return recursion(s, l + 1, r - 1)

def is_palindrome(s):
    recursion(s, 0, len(s) - 1)

for i in string_list:
    count = 0 # global을 썻으므로 for문이 돌때마다 초기화해야함
    is_palindrome(i)
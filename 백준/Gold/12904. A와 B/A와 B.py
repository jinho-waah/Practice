import sys
from collections import defaultdict, deque
input = sys.stdin.readline
sys.setrecursionlimit(2000)

# 입력 처리
# N = input().strip()

word1 = input().strip()
word2 = input().strip()

word1_list = [i for i in word1]
word2_list = [j for j in word2]


while len(word1_list) != len(word2_list):
    if word2_list[-1] == 'A':
        word2_list.pop()
    elif word2_list[-1] == 'B':
        word2_list.pop()
        word2_list.reverse()



if word1_list == word2_list:
    print(1)
else:
    print(0)
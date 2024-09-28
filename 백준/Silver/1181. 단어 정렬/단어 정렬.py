import sys
input = sys.stdin.readline

# 입력받기
N = int(input().strip())
words = set()  # 중복 제거를 위해 set 사용

# 단어 입력받기
for _ in range(N):
    words.add(input().strip())  # 중복을 제거하며 단어를 저장

# 정렬하기: 길이 우선, 길이가 같다면 사전 순
sorted_words = sorted(words, key=lambda x: (len(x), x))

# 출력하기
for word in sorted_words:
    print(word)

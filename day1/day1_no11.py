first_set = set([1,2,3,4])
second_set = set([1,3,5,6,7])

print(first_set)                # {1, 2, 3, 4}
print(second_set)               # {1, 3, 5, 6, 7}
print(first_set | second_set)   # {1, 2, 3, 4, 5, 6, 7} 합지합
print(first_set & second_set)   # {1, 3} 교집합
print(first_set - second_set)   # {2, 4} 차집합
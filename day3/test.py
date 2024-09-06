people = [("조진호", 32), ("최진영", 28), ("손호성",30), ("김세연",26)]
new_peoople = sorted(people, key=lambda person: person[1])
print(new_peoople)

print("=====================================================")
furit_dict = { 'banana':8, 'melon': 2, 'apple': 6, 'kiwi': 5}
print(furit_dict)
# 딕셔너리 키값 a ~ z
sortted1_dict = sorted(furit_dict.items(), key=lambda x: (x[0], -x[1]))
sortted2_dict = sorted(furit_dict.items(), key=lambda x: (x[0], x[1]))

# 딕셔너리 value 값 순서
sortted3_dict = sorted(furit_dict.items(), key=lambda x: (x[1], x[0]))
sortted4_dict = sorted(furit_dict.items(), key=lambda x: (-x[1], x[0]))

print(sortted1_dict)
print(sortted2_dict)
print(sortted3_dict)
print(sortted4_dict)
print("=====================================================")
num = [1,2,3,4,5,6]

result1 = list(map(lambda x: x * 2,num))
result2 = list(filter(lambda x : x % 2 ==0, num))
print(result1)
print(result2)

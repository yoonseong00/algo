my_list = [1,5,8,3,3,2,5,6,5,4]

counter = [0 for i in range(len(my_list))]

for num in my_list:
    counter[num] += 1

# print(counter)

result = []

for value,count in enumerate(counter):
    # print(value, count)
    for i in range(count):
        result.append(value)

print(result)

# counting 정렬은 원래 데이터를 각 숫자별로 몇개가 나왔는지 체크하고 그걸 나열하는 방식이다.
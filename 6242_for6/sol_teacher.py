blood_list = ['A', 'A', 'A', 'O', 'B', 'B', 'O', 'AB', 'AB', 'O']

blood_dict = {
    'A': 0,
    'O': 0,
    'B': 0,
    'AB': 0,
}

for blood in blood_list:
    blood_dict[blood] += 1

print(blood_dict)


#새로운 데이터를 추가하면 위 코드에서는 작동을 하지 않는다.
#위 문제를 해결하기 위해 아래와 같은 방식 참고
# dict = {}를 만들고 for문을 돌려 if a in list명.keys():는 dict[]+=1을 통해 개수 추가, else에는 dict[]=1로 해서 새로 받은 값을 1로 지정해주는 코드로 만들면 된다.


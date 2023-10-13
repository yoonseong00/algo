my_list = [1,7,6, 5, 3, 7, 4, 10, 4, 5, 2]


for i in range(len(my_list)-1, 0 ,-1):
    for j in range(i):
        left = my_list[j]
        right = my_list[j+1]

        if left > right:
            my_list[j], my_list[j+1] = my_list[j+1], my_list[j]
    

print(my_list)
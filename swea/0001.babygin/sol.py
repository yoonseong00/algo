import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    numbers = input()
    # count_list = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    count_list = [0 for i in range(10)]

    

    for number in numbers:
        count_list[int(number)] += 1

    idx = 0
    is_babygin = 0
    
    while idx < len(count_list):
        #1. triple인지 검증
        if count_list[idx] >= 3:
            count_list[idx] -= 3
            is_babygin += 1
        
        #2. run인지 검증
        if idx < len(count_list) - 2:
            if count_list[idx] and count_list[idx+1] and count_list[idx+2]:
                is_babygin += 1
                count_list[idx] -= 1
                count_list[idx+1] -= 1
                count_list[idx+2] -= 1

        idx += 1
    if is_babygin == 2:
        print(True)
    else:
        print(False)



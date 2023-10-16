# 한 루프를 돌때 (가장 높은 값에서 낮은 값에 값을 줘야한다) 이렇게 작동을 해야함
# 문제에서 루프를 다 돌았을 때 가장 큰 값과 작은 값의 차이를 구하는 것이 핵심
# 즉, 원래 모형을 유지 안하고 sort를 시켜 가장 큰 값을 작은 값에 줘도 될거같은데

import sys
sys.stdin = open('input.txt')

T = 10


for tc in range(1, T+1):
    dump = int(input())            #N은 반복해야할 횟수

    Num_list = list(map(int, input().split()))

    arr1 = []
    arr2 = []

    for i in range(dump+1):
        Num_list.sort() # 한번 반복할때마다 내림차순으로 정렬
        arr1.append(Num_list[-1])   #최댓값을 arr1에 넣기
        arr2.append(Num_list[0])    #최소값을 arr2에 넣기

        Num_list[-1] -= 1   # 최대값에서 -1
        Num_list[0] += 1    # 최소값에서 +1

        if Num_list[-1] - Num_list[0] < 1:  # 만약 더이상 루프를 돌 필요가 없을 때 정지
            break
    
    top = arr1[int(dump+1)-1]
    bottom = arr2[int(dump+1)-1]

    print(f'#{tc} {top-bottom}')


    
    


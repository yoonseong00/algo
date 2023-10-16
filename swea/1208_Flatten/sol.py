import sys
sys.stdin = open('input.txt')

T = 10


for tc in range(1, T+1):
    dump = int(input())            #N은 반복해야할 횟수

    Num_list = list(map(int, input().split()))

    for j in range(dump):
        num_max = Num_list[0] #최대값 구하기
        max_idx = 0
        num_min = Num_list[0] #최소값 구하기
        min_idx = 0
        for i in range(100):
            if num_max < Num_list[i]:
                num_max = Num_list[i]
                max_idx = i
            if num_min > Num_list[i]:
                num_min = Num_list[i]
                min_idx = i

        Num_list[max_idx] -=1
        Num_list[min_idx] +=1

        # 전체 평탄화 횟수 전에 평탄화가 완료된 경우
        if Num_list[max_idx] - Num_list[min_idx] < 1:
            break

    result = max(Num_list) - min(Num_list)

    print(f'#{tc} {result}')
        

    
        



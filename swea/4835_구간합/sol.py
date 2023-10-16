import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N, M = list(map(int, input().split()))      # N은 정수가 들어있는 배열 갯수, M은 묶어야할 범위 

    numbers = list(map(int, input().split()))   #배열된 숫자 리스트

    Num_list= []

    for i in range(N-M+1): # 총 반복해야할 횟수 ex) 10개의 배열을 3개씩 묶어서 진행을 하면 8번 루프를 돌아야하니 N - M + 1
        result = 0
        for j in range(i, M+i): # M만큼 묶기
            result += numbers[j] # M만큼 묶은 값들의 합을 result에 저장

        Num_list.append(result) #3개씩 묶어서 합한 값들은 리스트에 추가
        

    
        
    print(f'#{tc} {max(Num_list)-min(Num_list)}')


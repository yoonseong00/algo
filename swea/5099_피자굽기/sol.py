import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N, M = list(map(int, input().split()))  # N = 화덕의 크기      M = 피자개수

    pizza = list(map(int, input().split()))

    cheeze = [] #인덱스와 함께 피자(치즈양)가 들어갈 list


    # input에서 들어온 치즈양에 인덱스를 더한다. 아니 왜 인덱스 없이는 동작이 안돌아가냐 개같게
    for i in range(M): 
        cheeze.append([i+1, pizza[i]])
    print(cheeze)

    in_pizza = cheeze[:N]   # 0~N번까지 화덕 안으로 들어간다.
    reamin_pizza = cheeze[N:]   # N이후에 들어가야할(남은)피자들은 따로 저장

    while len(in_pizza) > 1:
        count = in_pizza.pop(0) #피자 빼기
        count[1] //= 2  # count에 0번째는 인덱스
        if count[1] == 0:   # 치즈가 다 녹았으면
            if reamin_pizza:
                in_pizza.append(reamin_pizza.pop(0))    #남은 피자 첫 번째 인덱스에 있는 값을 없애고 그 값을 더해주면 된다.
        
        else:   # 다 안녹았으면
            in_pizza.append(count)
        
        
    print(f'#{tc} {in_pizza[0][0]}')

        
import sys
sys.stdin = open('input.txt')

T = int(input())



for tc in range(1, T+1):
    N , K = map(int, input().split()) # N = 부분 집합의 원소의 개수, sum = 부분 집합의 합

    numbers = [i for i in range(1, 13)]

    count = 0

    subsets = [[]]

    for i in range(1 << len(numbers)):
        temp = []
        for j in range(len(numbers)):
            if i & (1 << j):
                temp.append(numbers[j])


        if len(temp) == N and sum(temp) ==K:
            count += 1
        
    

    print(f'#{tc} {count}')

    



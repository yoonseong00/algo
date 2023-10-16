import sys
sys.stdin = open('input.txt')

T= 10

for tc in range(1, T+1):
    N = int(input()) # 건물 개수

    buildings = list(map(int, input().split())) #건물 높이 리스트

    result = 0

    for i in range(2, N-2): # 처음 2칸 마지막 2칸은 항상 높이가 0이라고 했으니 2번째 인덱스부터 시작해서 N-2번째 인덱스까지
        count_2 = buildings[i] - buildings[i-2]
        count_1= buildings[i] - buildings[i-1]
        count1 = buildings[i] - buildings[i+1]
        count2 = buildings[i] - buildings[i+2]
        if count_2 > 0 and count_1 > 0 and count1 > 0 and count2 > 0:
            result += min(count1, count2, count_2, count_1)

    print(f'#{tc}  {result}')
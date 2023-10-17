import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input()) #배열된 숫자 개수

    numbers = list(map(int, input().split()))   # 배열 된 리스트

    

    result = []

    for i in range(1, 11):  # '결과를 10개까지 출력하시오'라는 조건때문에 10번의 루프만 돌게끔 설정
        
        numbers.sort()  #주어진 배열을 오름차순으로 정렬
        
        a = i   #i를 따로 변수로 설정을 안해주면 NonType 에러가 뜨기 때문에 따로 변수에 저장
        
        if i % 2:               # 만약 i가 홀수이면 인덱스 -1번부터 차례대로 내려가게끔 출력
            result.append(numbers[-(a+1)//2])      
        
        if i % 2 == 0:          # 만약 i가 짝수이면 인덱스 1번부터 차례대로 올라가게끔 출력
            result.append(numbers[(a-2)//2])

    a = ' '.join(str(s) for s in result)    #문제 출력 결과를 보면 list가 아닌 문자열로 나와있어 결과를 문자열로 변환하는 작업
      
    

    print(f'#{tc} {a}')

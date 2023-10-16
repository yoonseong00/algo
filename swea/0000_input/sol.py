import sys
sys.stdin = open('input.txt')

TC = int(input())

for i in range(TC):
    num = int(input())
    if num % 2:
        print('홀수')
    else:
        print('짝수')


# numbers = input().split()

# print(numbers)
# print(type(numbers))

# for number in numbers:
#     int_num = int(number)
    
#     if int_num % 2 == 1:
#         print(f'{int_num}은 홀수입니다.')


########################################################


numbers = list(map(int, input().split()))
# map은 반복은 도와주는 역할 ex)위같은 경우 문자로 되어있는 1,2,3,4,5를 int로 바꿔주는걸 반복한다.
# map은 list로 바꿔주기 전까지는 연산이 되지 않음.

for number in numbers:
    if number % 2:
        print(f'{number}은 홀수입니다.')



# 2차원 리스트 입력

N= int(input())

matrix = []

for i in range(N):
    numbers = list(map(int,(input().split())))

    matrix.append(numbers)

# 데이터 자체를 반복
# for row in matrix:    #열과 행으로 요소 출력
#     for item in row:

#행 우선 방식 (index 접근)
# for i in range(len(matrix)): # 인덱스로 2차원 배열 찾기
#     for j in range(len(matrix[0])):  
#         print(i,j,matrix[i][j])

# 열 우선 반복(index 접근)
for i in range(len(matrix)): # 인덱스로 2차원 배열 찾기
    for j in range(len(matrix[0])):  
        print(j,i,matrix[j][i])
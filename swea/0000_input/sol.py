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
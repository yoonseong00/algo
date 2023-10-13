import sys

sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input())

    numbers = list(map(int, input().split()))

    # min_number = 100000000000
    min_number = numbers[0]
    # max_number = 0
    max_number = numbers[0]

    for num in numbers:
        if num < min_number:
            min_number = num
        else:
            max_number = num

    result = max_number - min_number
    
    print(f'#{tc} {result}')
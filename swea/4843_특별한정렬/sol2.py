# sort 사용하지 않고 선택 정렬로 문제 풀어보기
import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input()) #배열된 숫자 개수

    numbers = list(map(int, input().split()))   # 배열 된 리스트

    result = []

    while True:
        max_num = 0
        for i in range(len(numbers)):
            if numbers[i] > max_num:
                max_num = numbers[i]
        result.append(max_num)
        numbers.remove(max_num)
            
        min_num = 100000000
        for j in range(len(numbers)):    
            if numbers[j] < min_num:
                min_num = numbers[j]
        result.append(min_num)
        numbers.remove(min_num)
        
        if len(result) == 10:
            break

    print(result)
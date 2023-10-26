def solution(hp):

    answer = (hp//5)+((hp%5)//3)+(((hp%5)%3)//1)
            
    return answer


print(solution(23))

#divmode(hp, 5or3or1)을 넣어서 몫은 더하고 나머지는 원래 계산한 값보다 작은 수로 다시 divmod에 넣어 계산
# 머쓱이네 피자가게는 피자를 일곱 조각으로 잘라 줍니다. 
# 피자를 나눠먹을 사람의 수 n이 주어질 때, 모든 사람이 피자를 한 조각 이상 먹기 위해 
# 필요한 피자의 수를 return 하는 solution 함수를 완성해보세요.

def solution(n):

        answer = 1
        
        if n % 7 ==0:
            answer = answer + (n//7) - 1  #사람 수가 만약 7의 배수는 한판을 추가하지 않아도 된다.
        elif (n // 7) > 1:                #만약 21명의 사람이 피자를 먹는다고 할 때, 첫 번째 줄 if 문이 없으면 한판을 더 가져가게 되는 오류가 발생
            answer = answer + (n//7)
        else:
            answer = 1

        return answer

print(solution(7))
print(solution(1))
print(solution(15))
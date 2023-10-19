def solution(sides):

    # 삼각형의 조건 두 변의 길이의 합 > 가장 긴 변의 길이
    # 1번째 케이스 slides의 요소 중 가장 큰 값이 가장 긴 변이라고 할 때 : 작은 요소와 큰 요소 사이의 값들이 가능
    # 2번째 케이스 두 요소의 합보다 작고 요소 중 큰 값 사이에도 가능

    return 2*min(sides)-1

print(solution([1,2]))
print(solution([3,6]))
print(solution([11,7]))
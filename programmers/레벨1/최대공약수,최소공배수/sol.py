def gcd(a, b):
    for i in range(min(a, b), 0, -1):
        if a % i == 0 and b % i == 0:
            return i

def lcm(a, b):
    for j in range(max(a,b), (a*b)+1):
        if j % a ==0 and j % b == 0:
            return j

def solution(n, m):

    return [gcd(n, m), lcm(n, m)]
    
print(solution(2, 5))
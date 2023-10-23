def solution(price, money, count):
    
    don = 0
    
    for i in range(1, count+1):
        don += price * i

    if money > don:
        return 0
    else:
        return don - money

print(solution(3,20,4))
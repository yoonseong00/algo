def solution(chicken):

    coupon = 0
    
    while chicken >= 10:
        div, mod = divmod(chicken, 10)  # div = 몫 mod = 나머지

        coupon += div # 몫만큼을 쿠폰으로 반환
        chicken = div + mod # 몫 과 나머지의 합 = 총 시켜먹을 수 있는 치킨 마릿수

    
    return coupon

print(solution(108))
print(solution(1081))



# 치킨 1마리당 쿠폰 1장 
# 쿠폰 10장에 치킨 한마리
# 근데? 미친 가게가 서비스 치킨에도 쿠폰을 준다
# ex: 1.1081마리 주문
#     2.쿠폰 1081장 발급 -> 108마리 주문 가능(108장 저장) + 1장
#     3. 108마리 주문-> 108장 쿠폰 지급
#     4. 10마리 주문 -> 10장 쿠폰(10장 저장) 지급
#     5. 10장으로 1마리 주문 -> 1장 발급

#     대충 쿠폰을 저장해놓을 변수하나 만들고
#     그 변수에 1마리 치킨을 주문할때마다 -10장 + 1장

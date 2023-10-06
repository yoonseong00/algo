#100~300 사이의 숫자에서 각각의 자리 숫자가 짝수인 숫자를 찾아 콤마(,)로 구분해 출력하는 프로그램을 작성하십시오.

num = []

for i in range(100,301):
    a = int(i/100)
    b = int(i/10) 
    if i % 2 == 0 and b % 2 == 0 and a % 2 == 0:
        num.append(str(i))

print(",".join(num))
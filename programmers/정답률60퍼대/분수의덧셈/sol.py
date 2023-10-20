from fractions import Fraction

def solution(numer1, denom1, numer2, denom2):

    a = Fraction(numer1,denom1)
    b = Fraction(numer2, denom2)
    result = a + b

    bunsu = result.numerator

    bunza = result.denominator

    answer = [bunsu, bunza]

    return answer

print(solution(1,2,3,4))
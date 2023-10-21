def solution(bin1, bin2):
    
    return (bin(int(bin1, 2) + int(bin2, 2))[2:])   # bin 옆에 2라는 숫자는 2진수라는걸 의미

print(solution("10","11"))
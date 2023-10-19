import sys
sys.stdin = open('input.txt')

T = int(input())

def paper(number):

    if number % 10 == 0:
        if number == 10:    # number가 10이면 1이 확정
            return 1
        elif number == 20:  # number가 20이면 3이 확정
            return 3
        else:
            return paper(number-10) + 2*paper(number-20)    #엑셀로 모든 경우의 수를 보니 a2 + 2a1 규칙이 나와 적용



for tc in range(1, T+1):
    N = int(input())

    answer = paper(N)

    print(f'#{tc} {answer}')


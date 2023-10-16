import sys
sys.stdin = open('input.txt')

T = int(input())

def loop(page, target):

    left = 1

    right = page

    count = 1

    while left <= right:
        C = int((left+right)/2)
        if C == target:
            return count
                

        elif C > target:
            right = C -1 
            count += 1
                
        elif C < target:
            left = C + 1
            count += 1
    

for tc in range(1, T+1):
    page, A, B = map(int, input().split()) #P=전체 페이지 수 , A = A가 찾아야 할 페이지, B = B가 찾아야 할 페이지

    Count_A = loop(page, A) 
    Count_B = loop(page, B)

    if Count_A > Count_B:
        result = 'B'
    elif Count_A < Count_B:
        result = 'A'
    else:
        result = 0
    
    print(f'#{tc} {result}')
        

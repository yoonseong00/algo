#이 문제의 핵심은 '부분집합' 즉 숫자가 나란히 있는 경우가 아닌 N만큼의 개수를 뽑아 K가 나오게 하는 모든 경우의 수를 구해야한다.

import sys
sys.stdin = open('input.txt')

from itertools import combinations

T = int(input())

numbers = [i for i in range(1, 13)]

for tc in range(1, T+1):
    N , K = map(int, input().split()) # N = 부분 집합의 원소의 개수, sum = 부분 집합의 합

    combi = list(combinations(numbers, N))
    count = 0
    for i in combi:
        if sum(i) == K:
            count+=1
    print(f'#{tc} {count}')

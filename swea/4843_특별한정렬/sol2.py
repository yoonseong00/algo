# sort 사용하지 않고 선택 정렬로 문제 풀어보기
import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input()) #배열된 숫자 개수

    numbers = list(map(int, input().split()))   # 배열 된 리스트

    
import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):

    K, N, M = list(map(int, input().split()))  #설명에 나와있듯 첫번째는 K(1회 충전 당 이동할 수 있는거리), N(도착해야하는 위치), M(정류소 갯수)

    charge_station = list(map(int, input().split()))  #charge_station을 호출했으니 사실상 M이라는 변수는 이제 생각 안해도 될듯

    count = 0

    current = 0

    while current + K < N:  #현재위치에서 한번에 이동 가능한 K를 합한 값이 내가 도착해야하는 위치보다 클 때 루프 종료

        for move in range(K, 0, -1): #K만큼 움직이다 충전소가 있는 K-(가장 작은 수)에 충전소가 있으면 충전을 해야하니 K~0까지 -1
    
            if (current + move) in charge_station: 
                current += move                     #현재위치에서 충전소까지 이동했으니 현재 위치는 충전소이다.
                count += 1                          #충전소에서 충전을 했으면 1회 count

                break
        else:
            count = 0
            break
    
    print(f'#{tc} {count}')

# 코드작성 전 메모장에 끄적인 것들

# K = 한번 충전으로 이동할 수 있는 정류장 수
# N = 0번에서부터 이동해야하는 거리
# M = 충전기가 설치된 정류장 개수


# 대충 K만큼 숫자가 증가하는데 거기에 도달하기 전 충전을 할 수 있는 곳이 있으면 해야되고,

# 만약? K만큼 가는 길 사이에 충전소가 없으면  0를 반환해야한다.



# ````````````````````````````````````
# 현재위치에서 K(충전해서 이동할 수 있는 거리)를 합한 값이 N보다 작을 때 
# 충전소에 충전을 하고 이동을 해야한다.

# 그럼.. 대충 current+move < N 이 루프를 도는 곳에서

# 현재위치에서 K칸씩 이동을 하는데 충전소를 만나면 충전

# 여기서 K칸씩 이동하는데 ex:2번 3번이 동시에 있을 때 3번에서 할 수 있으면 3번에서 해야하니까

# range(K, 0 ,-1) 루프를 돌려서 만약 충전소 리스트안에 있는 번호와 저 루프가 만나면

# 충전을 했으니 count에 1씩 추가

# 그리고 충전을 한 위치까지 이동을 했으니 현재위치에서 충전소까지 도착한 거리만큼 +해주기

    
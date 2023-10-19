import sys
sys.stdin = open('input.txt')
from pprint import pprint

T = int(input())

for tc in range(1 ,T+1):
    # V= 노드수 , E = 간선 수
    V, E = list(map(int, input().split()))

    nodes = [[0 for _ in range(V+1)] for _ in range(V+1)]

    for _ in range(E):
        node = list(map(int, input().split()))
        start = node[0]
        end = node[1]

        nodes[start][end] = 1

    # pprint(nodes)
    # S = 시작점 , G = 도착점
    S, G = list(map(int, input().split()))

    # nodes => 그래프 표현 (인접행렬)

    # 방문 체크리스트
    check_list = [False] * (V+1) # F로 나열된 리스트에 방문을 했으면 F를 True 바꿔줌

    #dfs 용 스택
    stack = []

    # v 부터 시작
    v = S
    check_list[v] = True # 시작점은 이미 방문을 한 상태이므로 check_list에 True로 설정
    stack.append(v) #stack에 지나간 곳들에 대한 정보를 넣어야하므로 시작점인 v를 일단 stack에 넣고 시작

    result = 0

    while len(stack):
        for w in range(V+1):    #v는 현재 위치고 w는 어디까지 갈 수 있는지 표기
        # 연결된 것을 체크
            if nodes[v][w] == 1:    #시작점을 기준으로 1이 있는 곳 확인
                #아직 방문 안했다면
                # => 체크리스트가 False라면
                if not check_list[w]:
                    # 현재 나의 위치 v를 stack에 push
                    stack.append(v)
                    check_list[w] = True
                
                    # w를 현재 위치로 변경
                    v = w

                    if w == G:
                        result = 1
                    
                    break
        
        #break를 만나지 않은 경우
        # => 방문하지 않은 정점이 없는 경우
        # => 과거의 위치로 돌아가기(pop을 통해서 stack에서 빼낸 값으로 이동)
        else:
            v = stack.pop()

    print(f'#{tc} {result}')

                    

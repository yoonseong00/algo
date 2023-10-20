import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    # V = 노드 수 , E = 간선 수
    V, E = list(map(int, input().split()))

    nodes = [[0] * (V+1) for _ in range(V+1)]

    for _ in range(E):
        node = list(map(int, input().split()))

        start = node[0]
        end = node[1]

        nodes[start][end] = 1
        nodes[end][start] = 1

    S , G = list(map(int, input().split()))

    # 방문 체크용 리스트
    check_list = [False] * (V+1)

    # bfs를 위한 queue
    queue = []

    #거리 계산을 위한 list
    distance = [0] * (V+1)

    # 시작 전 시작 노드를 저장
    now = S
    check_list[now] = True
    queue.append(now)

    while len(queue):
        now = queue.pop(0)
        check_list[now] = True

        # now와 연결되어있는 다른 노드를 순회
        for link in range(V+1):
            if nodes[now][link] == 1:

                # 아직 방문하지 않은 node가 있다면
                if not check_list[link]:
                    queue.append(link)

                    # 이전 노드의 거리 + 1
                    distance[link] = distance[now] + 1
    
    print(distance[G])

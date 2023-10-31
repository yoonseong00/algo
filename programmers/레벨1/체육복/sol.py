# def solution(n, lost, reserve):
#     # n = 학생 수 , lost = 피해자 , reserve = 구세주

#     sort_lost = sorted(lost)
#     sort_reserve = sorted(reserve)

#     # 도난을 당했으나 본인 것은 잘챙긴 사람들은 for문에서 제외

#     for j in range(1, n+1):
#         if j in reserve and j in lost:
#             sort_reserve.remove(j)
#             sort_lost.remove(j)
#     print(sort_lost)
#     print(sort_reserve)

#     # 구세주의 앞 또는 뒤에 사람이 피해자라면 체육복 빌려주기
#     for i in sort_reserve:
#         if i-1 in sort_lost:
#             sort_lost.remove(i-1)
#         elif i+1 in sort_lost:
#             sort_lost.remove(i+1)

#     return n - len(sort_lost)

def solution(n, lost, reserve):
    # n = 학생 수 , lost = 피해자 , reserve = 구세주

    lost
    reserve.sort()

    # 도난을 당했으나 본인 것은 잘챙긴 사람들은 for문에서 제외

    for j in range(1, n+1):
        if j in reserve and j in lost:
            reserve.remove(j)
            lost.remove(j)

    # 구세주의 앞 또는 뒤에 사람이 피해자라면 체육복 빌려주기
    for i in reserve:
        if i-1 in lost:
            lost.remove(i-1)
        elif i+1 in lost:
            lost.remove(i+1)

    return n - len(lost)

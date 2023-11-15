def solution(id_list, report, k):
    # 받은 신고 횟수를 저장하는 dict
    reported_count = {}
    # 누구로부터 신고를 받았는지 저장하는 dict
    reported_by = {}

    for r in report:
        reporter, reported = r.split()
        
        # 만약 신고된 유저가 reported_by에 없다면 빈 집합으로 reset
        if reported not in reported_by:
            reported_by[reported] = set()
        
        # 신고자가 중복으로 신고하지 않았다면 해당 유저의 신고 횟수 증가 및 신고자 기록
        if reporter not in reported_by[reported]:
            # 해당 유저의 신고 횟수 1 증가
            reported_count[reported] = reported_count.get(reported, 0) + 1
            # 해당 유저를 신고한 사람 기록
            reported_by[reported].add(reporter)

    # 정지된 유저들 찾기 (신고 횟수가 k 이상인 유저) 
    stopped_users = set()
    for user, count in reported_count.items():
        if count >= k:
            stopped_users.add(user)

    # 각 유저별로 결과 메일 수를 계산하여 리스트에 담기
    mails_sent = []
    for user in id_list:
        count = 0
        for stopped_user in stopped_users:
            if user in reported_by[stopped_user]:
                count += 1
        mails_sent.append(count)

    return mails_sent


print(solution(["muzi", "frodo", "apeach", "neo"],["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"],2))
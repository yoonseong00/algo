# 모든 달은 28일까지 있다고 가정합니다.
# temrs을 거친 기간이 오늘이라면 파기 x
# 파기해야할 정보를 리턴
# 구분점은 띄어쓰기

def Datetime(date):
    year, month, day = map(int, date.split('.'))
    return (year*12*28) + (month*28) + day
   
def solution(today, terms, privacies):
    answer = []

    # year, month, day = map(int, today.split('.'))

    # today = (year*12*28) + (month*28) + day

    today = Datetime(today)

    TermData = {}

    for i in terms:
        i = i.split()
        TermData[i[0]] = int(i[1])*28
    # for privacy in privacies:
    for privacy in range(len(privacies)):
        # date, term = privacy.split(' ')
        date, term = privacies[privacy].split()
        if Datetime(date) + TermData[term] <= today:
        # a = Datetime(date) + TermData[term]
        # print(a, today)
            # answer.append(privacies.index(privacy)+1)
            answer.append(privacy+1)

    return answer





print(solution("2022.05.19",["A 6", "B 12", "C 3"],["2021.05.02 A", "2021.07.01 B", "2022.02.19 C", "2022.02.20 C"]))
print(solution("2020.01.01",["Z 3", "D 5"],["2019.01.01 D", "2019.11.15 Z", "2019.08.02 D", "2019.07.01 D", "2018.12.28 Z"]))
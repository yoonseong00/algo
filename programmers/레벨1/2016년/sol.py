import datetime

def solution(a, b):
    week = ['MON','TUE','WED','THU', 'FRI', 'SAT', 'SUN']


    day = datetime.date(2016, int(a), int(b))
    
    answer = week[day.weekday()]

    return answer


print(solution(5,24))
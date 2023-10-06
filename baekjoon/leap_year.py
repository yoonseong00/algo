#윤년 구하기

year = int(input('연도를 입력하세요: 단, 1보단 크고 4000보단 작아야합니다.'))


if year % 4 == 0 and year % 100 == 0 and year % 400 == 0:
     print('1')
else:
    print('0')
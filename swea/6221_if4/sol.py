import sys
sys.stdin = open('input.txt', encoding='utf-8')

man1 = input()
man2 = input()

tc = ['가위', '바위', '보']

if tc.index(man1) == tc.index(man2) :
    print('Result : Draw')
elif (tc.index(man1) - tc.index(man2)) == 1 :
    print('Result : Man1 Win!')
elif (tc.index(man2) - tc.index(man1)) == 1 :
    print('Result : Man2 Win!')
else :
    if tc.index(man1) == 0 :
        print('Result : Man1 Win!')
    else :
        print('Result : Man2 Win!')
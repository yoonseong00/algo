import sys
sys.stdin = open('input.txt', encoding='utf-8')

man1 = input()
man2 = input()

rcp = ['가위', '바위', '보']

man1_idx = rcp.index(man1)
man2_idx = rcp.index(man2)

reuslt = man1_idx - man2_idx

if reuslt == 0:
    print('Result : Draw')
elif reuslt > 0:
    print(f'Result : Man{reuslt}Win!')
else:
    if reuslt == 1:
        print('Result : Man2 Win!')
    else:
        print('Result : Man1 Win!')
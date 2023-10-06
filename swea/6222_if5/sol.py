import sys
sys.stdin = open('input.txt')

a = input()

if a.isalpha():
    
    if a.isupper() :
        change = a.lower()
        print(f'{a}(ASCII:{ord(a)}) => {change}(ASCII:{ord(change)})')
    else:
        change = a.upper()
        print(f'{a}(ASCII:{ord(a)}) => {change}(ASCII:{ord(change)})')
else :
     print(a)   
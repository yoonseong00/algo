def solution(my_string):
    answer = ''
    vowels = 'aeiou'

    for vowel in vowels:
        my_string = my_string.replace(vowel, '')
        answer = my_string
    
    return answer

print(solution('bus'))
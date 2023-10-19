def solution(numbers):

    num_list = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

    for index, num in enumerate(num_list):
        numbers = numbers.replace(num, str(index))

    return int(numbers) # int로 안하면 str로 출력

print(solution("onetwothreefourfivesixseveneightnine"))
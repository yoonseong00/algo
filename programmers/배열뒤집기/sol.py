def solution(word):
    words = list(word)
    pals = []
    for i in range(len(words) - 1, -1, -1):
        pals.append(words[i])

    return pals

print(solution([1, 2, 3, 4, 5]))
print(solution([1, 1, 1, 1, 1, 2]))
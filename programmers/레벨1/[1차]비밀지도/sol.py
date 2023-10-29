def solution(n, arr1, arr2):

    secret = []

    for i in range(n):
        arr_bin = bin(arr1[i] | arr2[i])

        arr_bin = arr_bin[2:].zfill(n)

        arr_bin = arr_bin.replace('1', '#')

        arr_bin = arr_bin.replace('0', ' ')

        secret.append(arr_bin)


    return secret

print(solution(5, [9, 20, 28, 18, 11], [30, 1, 21, 17, 28]))
print(solution(6,[46, 33, 33 ,22, 31, 50],[27 ,56, 19, 14, 14, 10]))
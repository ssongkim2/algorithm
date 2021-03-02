word = 'abcde'

reversed_word = ''


# for i in range(len(word)):
#     reversed_word += word[len(word)-i-1]

def reversed_words(x):
    # result = x
    # n = 0
    # while n <= len(result):
    #     return result[n]+ reversed_words(n-1)
    #

    idx = len(x) - 1
    r_word = ''
    while idx >= 0:
        r_word += word[idx]
        idx -= 1
    return r_word




print(reversed_words(word))

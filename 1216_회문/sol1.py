import sys
sys.stdin = open('input.txt')

# T = int(input())
# for tc in range(1, T+1):
#     start = datetime.now()
#     solution(input())
#     end = datetime.now()
#     print('#{} {}'.format(10 * 10**tc, end-start))

#전치행렬
def t_mat(N_list):
    row = len(N_list)
    col = len(N_list[0])
    B = [[0 for _ in range(row)] for _ in range(col)]
    for i in range(row):
        for j in range(col):
            B[j][i] = N_list[i][j]
    return B

for tc in range(1, 11):
    T = int(input())
    word = [0]*100
    char_len = 0
    max_len = []
    mat_list = []
    for idx in range(len(word)):
        word[idx] = str(input())


    for col in range(100):
        for row in range(100):
            for row2 in range(row, 100, 1):
                if word[col][row:row2] == word[col][row:row2][::-1]:
                    char_len = row2-row
                    max_len.append(char_len)
    mat_list = t_mat(word)

    # print(mat_list)
    for col in range(100):
        for row in range(100):
            for row2 in range(row, 100, 1):
                if mat_list[col][row:row2] == mat_list[col][row:row2][::-1]:
                    char_len = row2-row
                    max_len.append(char_len)

    # def sort_list()
    print('{} {}'.format(tc, max(max_len)))


    # for row in range(100):
    #     for col in range(100):
    #         for col2 in range(col, 101, 1):
    #             if word[col:col2][row] == word[col:col2][row][::-1]:
    #                 char_len = col2 - col
    #                 max_len.append(char_len)

    # print(max_len)

    """
    print(max_len[-1])
    """


    # def reverse_word(x):
    #     idx = len(x) - 1
    #     r_word = ''
    #     while idx >= 0:
    #         r_word += word[idx]
    #         idx -= 1
    #     return r_word
    # for idx in range(len(word)):
    #     word[idx] = str(input())
    # word_len = 0
    # max_len = 0
    # for col in range(len(word)):
    #     for row in range(len(word)):
    #         words = ''
    #         reversed_words = ''
    #         for row2 in range(row,len(word),1):
    #             words += word[col][row2]
    #             reversed_words = reverse_word(words)
    #             if words == reversed_words:
    #                 word_len = len(words)
    #                 if word_len>=max_len:
    #                     max_len = word_len
    # print(max_len)




    # def bruteForce(p, t): #처음 같은 문자열이 나오는것을 찾음
    #     i=0
    #     j=0
    #     m = len(p)  #찾는 패턴길이
    #     n = len(t)  #문자열 전체길이
    #     while j < m and i < n:
    #         if t[i] != p[j]:
    #             i = i-j
    #             j = -1
    #         i = i+1
    #         j = j+1
    #     if j == m:
    #         return i - m
    #     else:
    #         return -1
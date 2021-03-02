import sys
sys.stdin = open('GNS_test_input.txt')

T = int(input())
for tc in range(1,T+1):
    F = list(map(str, input().split()))
    words = list(map(str,input().split()))
    # print(words)
    cnt = [0]*10
    #cnt = [0 for _ in range(10)]

    for word in words:
        if word == 'ZRO':
            cnt[0] +=1
        if word == 'ONE':
            cnt[1] +=1
        if word == 'TWO':
            cnt[2] +=1
        if word == 'THR':
            cnt[3] +=1
        if word == 'FOR':
            cnt[4] +=1
        if word == 'FIV':
            cnt[5] +=1
        if word == 'SIX':
            cnt[6] +=1
        if word == 'SVN':
            cnt[7] +=1
        if word == 'EGT':
            cnt[8] +=1
        if word == 'NIN':
            cnt[9] +=1

        #이거 for문으로 인덱싱해서 비교하는 방법으로 하면 더 짧아짐

    result =[]
    word1 = ['ZRO','ONE','TWO','THR','FOR','FIV','SIX','SVN','EGT','NIN']
    for i in range(10):
        for idx in range(cnt[i]):
            result.append(word1[i])
    print('#{}'.format(tc))
    print('{}'.format(' '.join(map(str,result))))


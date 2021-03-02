import sys
sys.stdin = open('sample_input.txt')
T = int(input())
for tc in range(1, T+1):
    words = input()
    result = ''
    list1 = []
    list2 = []
    cmp = []
    total = 0
    # print(word)
    # s = stack()
    for word in words:
        if word == '(' or word == '{' or word == '[':
            list1.append(word)
        elif word == ')' or word == '}' or word == ']':
            list2.append(word)
    if len(list1) != len(list2):
        result = '0'
    else:
        for idx in range(len(list1)):
            if list1[idx] == '(' and list2[idx] == ')':
                cmp.append(1)
            if list1[idx] == '{' and list2[idx] == '}':
                cmp.append(1)
            if list1[idx] == '[' and list2[idx] == ']':
                cmp.append(1)

            else:
                cmp.append(0)

    for idx in range(len(cmp)):
        total += cmp[idx]
    if total == len(cmp):
        result = '1'
    else:
        result = '0'
    print(result)

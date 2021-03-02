T = int(input())

for tc in range(1,T+!):
    str1 = input()
    str2 = input()
    #키=문자, value = 카운트한 수
    my_dict = {}

    #키값은 set으로 중복을 짤라서 키값에 넣기
    for key in set(str1):
        my_dict[key] = 0
    #key값 세기     
    for key in str2:
        if key in my_dict:
            my_dict[key]+= 1

    ans = 0
    #최대 찾기
    for i in my_dict.values():
        if ans < i:
            ans = i
    print()

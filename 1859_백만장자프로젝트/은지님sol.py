import sys
sys.stdin = open('input.txt')
def millionaire(my_list):
    my_max = max(my_list)
    temp = []
    income = 0

    # 재귀 base case
    if len(my_list) == 1:
        return income

    for idx in range(0, len(my_list)):
        if my_list[idx] == my_max:
            # max 값이면 있던 것 다 판매
            for i in range(len(temp)):
                income += my_list[idx] - temp[i]
                #
            if idx == len(my_list)-1:
                return income
            else:
                # 그 뒤부터 다시 재귀
                return income + millionaire(my_list[idx+1:])

        else:
            # max 아니면 다 구매
            temp += [my_list[idx]]


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    my_list = list(map(int, input().split()))

    print('#{} {}'.format(tc, millionaire(my_list)))
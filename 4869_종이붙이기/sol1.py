import sys
sys.stdin = open('sample_input.txt')

def factorial(n1,n2):    #n1 시작수 n2갯수
    if n1 == n2:
        return n1
    else :
        return n1*factorial(n1-1)*2

T = int(input())
for tc in (1,1+T):
    numbers = int(input())
    number = numbers//10
    result = 0
    # bit = [1]*number
    # bit2 = [1]
    # for idx in range(len(bit),0,-1):
    #     bit
    for idx in range(1,len(number)//2):
        result = factorial(number,number-1)
    result1 =factorial()
    if number %2 == 0: #짝수라면
        1 + for




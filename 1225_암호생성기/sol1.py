import sys
sys.stdin = open('input.txt')

for tc in range(1,11):
    T = int(input())
    numbers = list(map(int, input().split()))
    queue = []
    for idx in range(len(numbers)):
        queue.append(numbers[idx])
    chk = 0
    idx = 0
    while True:
        chk = queue.pop(0)
        chk = chk - idx - 1
        if chk <= 0:
            chk = 0
            queue.append(chk)
            break
        queue.append(chk)
        idx += 1
        if idx >= 5:
            idx = idx%5
    print('#{} {}'.format(tc,' '.join(map(str,queue))))
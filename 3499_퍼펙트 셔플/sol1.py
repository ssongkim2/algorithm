import sys
sys.stdin = open('sample_input.txt')

def solution(deck):
    deck2 = []
    deck3 = []
    deck4 = []
    if len(deck) % 2 == 0:
        for idx in range(len(deck)//2):
            deck2.append(deck[idx])
            deck2.append(deck[idx+(len(deck)//2)])
        return deck2
    if len(deck) % 2 == 1:
        deck2 = deck[0:(len(deck)//2+1)]
        deck3 = deck[len(deck)//2+1:]
        for idx in range(len(deck)//2):
            deck4.append(deck2[idx])
            deck4.append(deck3[idx])
        deck4.append(deck2[-1])
        return deck4

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    deck = list(map(str, input().split()))
    result = solution(deck)
    print('{} {}'.format(tc,' '.join(map(str,result))))

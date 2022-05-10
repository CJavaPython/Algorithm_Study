import sys
from collections import defaultdict
#N개의 박스, M개의 색상
#조커는 색이 다른 카드를 보관해도 된다
#첫째 줄 박스의 개수 N, 카드 색상 종류 M
#둘째 줄부터 박스에 들어있는 카드 수 입력
#박스 주어지면, 문제 조건 만족하게 하는 최소 이동?
input = sys.stdin.readline
N, M = map(int,input().split())

card_list = []
card_spec = {}
#alphabet 이라는 dictionary에 미리 해당 숫자를 더한다.
for i in range(N):
    card = list(map(int, input().split()))
    card_list.append(card)
    for c in range(len(card)):
        card_spec[card[c]]=card_spec.get(card[c],0)+1

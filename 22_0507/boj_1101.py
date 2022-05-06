import sys
from collections import defaultdict


input = sys.stdin.readline

#박스의 개수 n 카드색상의개수 m
n,m = map(int,input().split())

max_card = 9

#박스 1개는 조커박스로 지정할수 있다.. .흠..dictionary의 key로 joker 하나 놓고 나머지는 그냥 색상으로 할까?

card_list = [list(map(int,input().split())) for _ in range(n)]
card_dic = defaultdict(list)


for i in card_list:
    for j in range(len(i)):
        if j not in card_dic.keys():
            card_dic[j] = i[j]
        
        else:
           card_dic[j] += i[j] 

print(card_dic)
import sys
from collections import defaultdict


input = sys.stdin.readline

n = int(input())
word_dict = defaultdict(list)

word = [list(input().rstrip()) for _ in range(n)]

for i in word:
    for j in range(len(i)):
        if i[j] not in word_dict.keys():
            word_dict[i[j]] = 10 ** (len(i)-(j+1))
        else:
            word_dict[i[j]] += 10 ** (len(i)-(j+1))
            

word_dict = dict(sorted(word_dict.items(), key = lambda x: x[1], reverse= True))


max_num = 9
answer = 0

for value in word_dict.values():
    answer += value * max_num
    max_num -= 1

print(answer)




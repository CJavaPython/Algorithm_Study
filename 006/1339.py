import sys
import math
#수학학원에서 단어수학푸는 숙제
#N개의 단어, 알파벳 대문자로만.
#각 알파벳 대문자를 0~9 중 하나로 바꿔서
#N개의 수를 합하는 문제
#같은 알파벳은 같은 숫자로 바꿔야하며, 두 개 이상의 알파벳이 같은 숫자로 바뀌어지면 안된다.
#N개의 단어가 주어졌을 때, 그 수의 합을 최대로 만드는 프로그램.
#ex : gcf + abedc
input = sys.stdin.readline
N=int(input())
words = []
alphabet = {}
#alphabet 이라는 dictionary에 미리 해당 숫자를 더한다.
for i in range(N):
    word = input().strip()
    words.append(word)
    for w in range(len(word)):
        alphabet[word[w]]=alphabet.get(word[w],0)+pow(10,len(word)-w-1)
result=0
for j in range(10):
    result+=max(alphabet.values()) * (10-j-1)
    alphabet[max(alphabet, key=alphabet.get)]=0
print(result)
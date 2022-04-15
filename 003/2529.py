import sys
input=sys.stdin.readline
k=int(input())
#ies = in equality sign
ies=list(input().split())
visited=[False]*10
result=[]
val=[]
def check(s,prev,cur):
    if s == '<':
        return prev<cur
    elif s == '>':
        return prev>cur
def bt(depth,prev):
    if depth>=k:
        result.append("".join(val))
        return
    for i in range(10):
        if not visited[i]:
            if check(ies[depth], prev, i):
                val.append(str(i))
                visited[i]=True
                bt(depth+1,i)
                visited[i]=False
                val.pop()
    
for prev in range(10):
    val.append(str(prev))
    visited[prev]=True
    bt(0,prev)
    visited[prev]=False
    val.pop()
result.sort()
print(result[len(result)-1])
print(result[0])
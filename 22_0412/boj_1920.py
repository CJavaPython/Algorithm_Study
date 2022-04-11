import sys

input = sys.stdin.readline

n = int(input())

arr_n = list(map(int,input().split()))
arr_n.sort()

m = int(input())
arr_m = list(map(int,input().split()))

def b_search(target):

    left = 0
    right = len(arr_n)-1

    while left <= right:

        middle = (left+right) // 2

        if target == arr_n[middle]:
            return True


        if target < arr_n[middle]:
            right = middle - 1

        else:
            left = middle + 1

    return False


for i in range(len(arr_m)):
    if b_search(arr_m[i]):
        print(1)
    else:
        print(0)






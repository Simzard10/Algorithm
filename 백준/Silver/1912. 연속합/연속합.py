import sys
sys.setrecursionlimit(300000) 

n = int(input())

arr = list(map(int, input().split()))

sum_val = arr[0]
max_val = arr[0]

def dp(i):
    global sum_val, max_val
    if i >= len(arr):
        return

    if ((sum_val + arr[i]) >= arr[i]):
        sum_val = sum_val + arr[i]
    else:
        sum_val = arr[i] 

    max_val = max(max_val, sum_val)
    dp(i+1)
dp(1)

print(max_val)
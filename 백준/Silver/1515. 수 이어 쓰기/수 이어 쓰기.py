import sys

nums = sys.stdin.readline().rstrip()
n = 0
idx = 0
found = False 

while not found:
    n += 1
    for s in str(n):
        if nums[idx] == s:
            idx += 1
            if idx >= len(nums):
                print(n)
                found = True 
                break 
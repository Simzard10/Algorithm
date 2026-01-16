N, K = map(int, input().split())

temp = input()

arr = []

for i in str(temp):
    arr.append(i)

count = 0
for i in range(len(arr)):
    if arr[i] == 'P':
        for j in range(i-K, i+K+1):
            if j >= 0 and j <= len(arr)-1 and arr[j] == 'H':
                arr[j] = '0'
                count +=1
                break

print(count)
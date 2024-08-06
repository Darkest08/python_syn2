def swapper(arr):
    l = len(arr)
    for i in range(l - 1):
        buffer = arr[i]
        arr[i] = arr[l-1]
        arr[l-1] = buffer

n = int(input())
arr = list(input().split(' '))

swapper(arr)

print(' '.join(arr))
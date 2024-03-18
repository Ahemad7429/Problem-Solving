# Buble sort
# Push the minimum to last.
# o(n^2) worst, Average 
# o(n) best

def buble_sort(arr, n):
    if n == 1: return
    j = 0
    while j<=n-2:
        if(arr[j] > arr[j+1]):
            temp = arr[j]
            arr[j] = arr[j+1]
            arr[j+1] = temp
        j+=1
    buble_sort(arr, n-1)

n = int(input("Enter recursive buble sort length: "))
array = []
for i in range(n):
    print('Enter Element: ', i, sep='')
    element = int(input())
    array.append(element)

buble_sort(array, n)
print(array)
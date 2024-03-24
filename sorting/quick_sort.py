def partition(arr, low, high):
    i = low
    j = high
    pivot = arr[low]

    while i < j:
        while arr[i] <= pivot and i <= high - 1:
            i+=1
        while arr[j] > pivot and j >= low + 1:
            j-=1
        if i < j:
            arr[i], arr[j] = arr[j], arr[i]
        
    arr[low], arr[j] = arr[j], arr[low]
    return j


def qs(arr, low, high):
    if(low < high):
        part = partition(arr, low, high)
        qs(arr, low, part - 1)
        qs(arr,  part + 1, high)


n = int(input("Enter Quick sort length: "))
array = []
for i in range(n):
    print('Enter Element: ', i, sep='')
    element = int(input())
    array.append(element)

qs(array, 0, n - 1)
print(array)
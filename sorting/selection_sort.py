# Selection sort
# Select Minimun and swap.
# o(n^2) worst, best

def selection_sort(arr, n):
    for i in range(n-1):
        min = i
        j = i
        while j <= n-1:
            if(arr[j] < arr[min]):
                min=j
            j+=1
        temp = arr[min]
        arr[min] = arr[i]
        arr[i] = temp
        
n = int(input("Enter selection sort length: "))
array = []
for i in range(n):
    print('Enter Element: ', i, sep='')
    element = int(input())
    array.append(element)

selection_sort(array, n)
print(array)
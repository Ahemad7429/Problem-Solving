# Insertion sort
# Take element and put it correct position.
# o(n^2) worst, Average 
# o(n) best

def insertion_sort(arr, n):
    for i in range(n):
        j = i
        while j > 0 and arr[j-1] > arr[j]:
            temp = arr[j]
            arr[j] = arr[j-1]
            arr[j-1] = temp
            j-=1

n = int(input("Enter insertion sort length: "))
array = []
for i in range(n):
    print('Enter Element: ', i, sep='')
    element = int(input())
    array.append(element)

insertion_sort(array, n)
print(array)
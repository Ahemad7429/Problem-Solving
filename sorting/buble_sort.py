# Buble sort
# Push the minimum to last.
# o(n^2) worst, Average 
# o(n) best

def buble_sort(arr, n):
    i = n-1
    numSwap = 0
    while i>=1:
        for j in range(i):
            if(arr[j] > arr[j+1]):
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp
                numSwap += 1
        i-=1
    print("numSwap: ", numSwap)

n = int(input("Enter buble sort length: "))
array = []
for i in range(n):
    print('Enter Element: ', i, sep='')
    element = int(input())
    array.append(element)

buble_sort(array, n)
print(array)
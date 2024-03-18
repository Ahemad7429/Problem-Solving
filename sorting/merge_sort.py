def merge(arr, low, mid, high):
    left = low
    right = mid+1
    temp = []
    while(left<=mid and right<=high):
        if(arr[left] <= arr[right]):
            temp.append(arr[left])
            left+=1
        else:
            temp.append(arr[right])
            right+=1

    while left <= mid:
        temp.append(arr[left])
        left+=1
    
    while right <= high:
        temp.append(arr[right])
        right+=1

    i = low
    while i <= high:
        arr[i] = temp[i - low]
        i +=1

def merge_sort(arr, low, high):
    if(low == high): return
    mid = (low + high) // 2
    merge_sort(arr, low, mid)
    merge_sort(arr, mid+1, high)
    merge(arr,low,mid,high)

n = int(input("Enter merge sort length: "))
array = []
for i in range(n):
    print('Enter Element: ', i, sep='')
    element = int(input())
    array.append(element)

merge_sort(array, 0, n-1)
print(array)
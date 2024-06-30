# https://leetcode.com/problems/pancake-sorting/description/

def pancakeSort(arr):
    result = []
    n = len(arr)
    for target in range(n, 1, -1):
        index = arr.index(target)
        if index != target - 1:
            if index != 0:
                result.append(index + 1)
                arr = arr[:index + 1][::-1] + arr[index + 1:]
            result.append(target)
            arr = arr[:target][::-1] + arr[target:]
    return result

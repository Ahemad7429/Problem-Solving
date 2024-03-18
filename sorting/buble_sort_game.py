class Solution:
    def game(self, a, b, n):
       aSwap = self.buble_sort_swap(a.copy(),n)
       bSwap = self.buble_sort_swap(b.copy(),n)

       if(aSwap == bSwap):
           print("Tie")
       elif (aSwap < bSwap):
           print(a)
       else:
           print(b)

    
    def buble_sort_swap(self, arr, n):
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
        return numSwap
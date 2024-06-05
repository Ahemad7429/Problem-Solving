def triangle(n:int) ->None:
    for i in range(1, n+1):
        for j in range(i):
            print(i, end=" ")
        print("")


# Sample Input 1:
# 3
# Sample Output 1:
# 1 
# 2 2 
# 3 3 3
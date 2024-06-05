# Sample Input 1:
# 3
# Sample Output 1:
# 1
# 1 2 
# 1 2 3

def nTriangle(n:int) ->None:
    for i in range(1, n+1):
        for j in range(i):
            print(j+1, end=" ")
        print("")

nTriangle(3)
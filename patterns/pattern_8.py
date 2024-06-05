# Sample Input 1:
# 3
# Sample Output 1:
# *****
#  ***
#   *

def nStarTriangle(n: int) -> None:
    for i in range(n):
        for _ in range(i):
            print(" ", end="")
    
        for _ in range(2*n - (2*i+1)):
            print("*", end="")

        for _ in range(i):
            print(" ", end="")
        print("")

nStarTriangle(3)
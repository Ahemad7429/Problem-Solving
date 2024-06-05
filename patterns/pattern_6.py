# Sample Input 1:
# 3
# Sample Output 1:
# 1 2 3
# 1 2
# 1

def nNumberTriangle(n: int) -> None:
    for i in range(1, n+1):
        for j in range(1, n - i + 2):
            print(j, end=" ")
        print("")
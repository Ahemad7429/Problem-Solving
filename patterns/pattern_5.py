# Sample Input 1:
# 3
# Sample Output 1:
# * * *
# * *
# *


def seeding(n: int) -> None:
    for i in range(n):
        for j in range(n-i):
            print("*", end=" ")
        print("")
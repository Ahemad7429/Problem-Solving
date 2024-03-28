# Prime Number in the Range
# Write a program that takes an integer N as input and prints all the prime numbers that lie in the range from 2 to N (inclusive). Each prime number should be printed on a separate line.

# Input Format:
# The input consists of a single integer N.

# Output Format:
# The program outputs the prime numbers in the range from 2 to N (inclusive), with each prime number printed on a separate line.

# Sample Input:
# 10
# Sample Output:
# 2
# 3
# 5
# 7
# Constraints:
# 1 <= N <= 1000

class Solution:
    def print_primes(num):
        for number in range(num):  
            if number > 1:  
                    for i in range(2, number):  
                        if (number % i) == 0:  
                            break  
                    else:  
                        print (number)

Solution.print_primes(10)
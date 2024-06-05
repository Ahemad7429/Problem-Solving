# Chocolate Distribution
# Dholu and Bholu are great fans of odd numbers, that's why they want to divide the chocolate in such a way that each of the two parts weighs odd number of grams, at the same time it is not obligatory that the parts are equal. The boys are extremely excited to start eating their chocolates as soon as possible, that's why you should help them and find out, if they can divide the chocolate in the way they want. For sure, each of them should get a part of positive weight.

# Input Format
# The first (and the only) input line contains integer number c (1 ≤ c ≤ 100) — the weight of the chocolate bought by the boys.

# Output Format
# Return True, if the boys can divide the chocolate into two parts, each of them weighing odd number of grams; and False in the opposite case

# Sample Input
# 5
# Sample Output
# NO
# Explanation
# In this case, the weight of the chocolate is 5. The condition for dividing the chocolate into two parts, each weighing an odd number of grams, is not satisfied. Hence, the output is "NO."
# Constraints
# 1 ≤ c ≤ 100: The weight of the chocolate bought by the boys.

class Solution:
    def canDivideChocolate(self, n):
      if n >= 2 and n % 2 == 0:
          return "YES"
      else:
          return "NO"
      


# Word Correction
# Tuntun is very upset that many people on the Net mix uppercase and lowercase letters in one word. That's why he decided to invent an extension for his browser that would change the letter's register in every word so that it either only consisted of lowercase letters or, vice versa, only of uppercase ones. At that as little as possible letters should be changed in the word. For example, the word HoUse must be replaced with house, and the word ViP — with VIP. If a word contains an equal number of uppercase and lowercase letters, you should replace all the letters with lowercase ones. For example, maTRIx should be replaced by matrix. Your task is to use the given method on one given word.

# Input Format
# The first line contains a word s — it consists of uppercase and lowercase Latin letters and possesses the length from 1 to 100.
# Ouput Format
# Print the corrected word s. If the given word s has strictly more uppercase letters, make the word written in the uppercase register, otherwise - in the lowercase one.
# Sample Input
# HoUse
# Sample Output
# house
# Explanation
# In this example, the word "HoUse" contains 2 uppercase letters ('H', 'U') and 3 lowercase letters ('o', 's', 'e'). Therefore, the output is "house".
# Constraints
# - The length of the word 's' is between 1 and 100 (1 ≤ |s| ≤ 100).
# - The word 's' consists of uppercase and lowercase Latin letters.
      
class Solution:
    def word_correction(self, s):
      upper_count = sum(1 for char in s if char.isupper())
      lower_count = sum(1 for char in s if char.islower())
  
      # Determine the correct case based on the counts
      if upper_count > lower_count:
          return s.upper()
      else:
          return s.lower()
      
# Board Filling
# You have given a rectangular board of M × N squares. You also have unlimited number of standard block pieces of  2 x1 squares. You are allowed to rotate the pieces. You are asked to place as many blocks as possible on the board so as to meet the following conditions:

# Each block completely covers two squares.

# No two blocks overlap.

# Each block lies entirely inside the board. It is allowed to touch the edges of the board.

# Find the maximum number of blocks, which can be placed under these restrictions.

# Input
# In a single line you are given two integers M and N — board sizes in squares.
# Output
# Output one number — the maximal number of block of wood, which can be placed.
# Sample Input
# 2 4
# Sample Output
# 4
# Explanation
# We are given the board of size 2x4 which is given as:
# ----
# ----

# We can place two blocks which are placed horizontally, in each row making a total of 4 in this way:
# ==
# ==

# Constraints
# 1 ≤ M ≤ N ≤ 16 
      

# class Solution:
#     def boardfill(self, n, m):
#       return (m * n) // 2
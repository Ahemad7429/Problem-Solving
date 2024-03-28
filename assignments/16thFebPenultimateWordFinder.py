
# Penultimate Word Finder
# Write a program that finds the penultimate word (next to last word) in a sentence.
# The program takes a sentence as input and outputs the penultimate word from the sentence.

# Input Format:
# The input consists of a single sentence containing words separated by spaces.

# Output Format:
# The program outputs the penultimate word from the input sentence.

# Sample Input 1:
# Learning programming is fun.
# Sample Output 1:
#  is
# Constraints:
# The sentence can contain alphabets, numbers, and special characters.
# The sentence will not be empty.
# The sentence will have at least two words.
# Explanation:
# The penultimate word is "the" as it is the next to last word in the sentence "She sells seashells by the seashore."

class Solution:
    def find_penultimate_word(self, sentence):
        n = len(sentence)
        last2ndWord = ""
        wordsArray = []
        for i in range(n-1, 0, -1):
            if(sentence[i] == " "):
                wordsArray.append(last2ndWord)
                last2ndWord = ""
                if(len(wordsArray) == 2):
                    break
            else:
                last2ndWord =  sentence[i] + last2ndWord
        print(wordsArray[1]) 

                
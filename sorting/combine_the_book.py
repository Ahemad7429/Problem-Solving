# Combine the Books
# In the enchanting village of Bookland, there are two mystical bookstores, Alara's Books and Balin's Reads.
# Your task is to create a program that combines their inventories into a single sorted list.

# Input:
# 4 4

# book enchanted spell wand

# ancient dragon magic scroll

# Output:
# ancient book dragon enchanted magic scroll spell wand

class Solution:
    def solve(inventory1, inventory2):
        array = inventory1 + inventory2
        array = sorted(array)
        return array

Solution.solve(['book', 'enchanted', 'spell', 'wand'],['ancient', 'dragon', 'magic' ,'scroll'])

# https://leetcode.com/problems/letter-combinations-of-a-phone-number/description/

def letterCombinations(digits):
    if not digits:
        return []
    
    # Mapping of digits to corresponding letters
    phone_map = {
        '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
        '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'
    }
    
    def backtrack(index, path):
        # If the path length is the same as digits length, add to results
        if index == len(digits):
            combinations.append(''.join(path))
            return
        
        # Get the letters that the current digit maps to, and loop through them
        possible_letters = phone_map[digits[index]]
        for letter in possible_letters:
            # Add the letter to the current path
            path.append(letter)
            # Move on to the next digit
            backtrack(index + 1, path)
            # Backtrack by removing the letter before moving to the next
            path.pop()
    
    combinations = []
    backtrack(0, [])
    return combinations

# Example usage:
print(letterCombinations("23"))  # Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]

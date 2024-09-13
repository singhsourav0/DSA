class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        output = []
        i, j = 0, 0
        while i < len(word1) and j < len(word2):
            output.append(word1[i])
            output.append(word2[j])
            i += 1
            j += 1
        
        # Add the remaining part of word1 or word2, if any
        if i < len(word1):
            output.extend(word1[i:])
        if j < len(word2):
            output.extend(word2[j:])
        
        return ''.join(output)

# Create an instance of the Solution class
solution = Solution()

# Sample inputs
word1 = input("abc")
word2 = input("pqr")

# Call the mergeAlternately method
result = solution.mergeAlternately(word1, word2)

# Print the result
print(result)  # Output should be "apbqcr"

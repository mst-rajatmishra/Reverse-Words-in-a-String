class Solution:
    def reverseWords(self, s: str) -> str:
        # Step 1: Trim the string to remove leading and trailing spaces
        s = s.strip()
        
        # Step 2: Split the string into words
        words = s.split()
        
        # Step 3: Reverse the list of words
        words.reverse()
        
        # Step 4: Join the words with a single space
        result = ' '.join(words)
        
        return result

# Example usage
if __name__ == "__main__":
    solution = Solution()
    print(solution.reverseWords("the sky is blue"))        # Output: "blue is sky the"
    print(solution.reverseWords("  hello world  "))         # Output: "world hello"
    print(solution.reverseWords("a good   example"))        # Output: "example good a"

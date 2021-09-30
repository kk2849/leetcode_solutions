class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        stack = 0
        min = 0
        
        for char in range(len(s)):
            if s[char] == '(':
                stack += 1
            else:
                # char == ')'
                if stack > 0:
                    stack -= 1
                else:
                    min += 1
        
        return min + stack
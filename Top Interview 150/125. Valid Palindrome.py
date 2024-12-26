class Solution:
    def isPalindrome(self, s: str) -> bool:
        c_text = ''.join(char.lower() for char in s if char.isalnum())
        i, j = 0, len(c_text)-1
        
        while i < j:
            if c_text[i] != c_text[j]:
                return False
            i+=1
            j-=1
        return True
    
sol = Solution()
print(sol.isPalindrome(s = "A man, a plan, a canal: Panama"))
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s_sentece = s.split()
        last_word = s_sentece[-1]
        length = 0
        for i in range(len(last_word)):
            length += len(last_word[i])
        return  length
    
    
sol = Solution()
print(sol.lengthOfLastWord(s = "Hello World"))
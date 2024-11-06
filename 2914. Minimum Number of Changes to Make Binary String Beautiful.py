class Solution:
    def minChanges(self, s: str) -> int:
        n = len(s)
        count = 0

        # i = 0
        # while i < n - 1:
        #     if s[i] + s[i+1] == '00' or s[i] + s[i+1] == '11':
        #         i += 2
        #     else:
        #         count += 1
        #         i += 2
            
        # return count
        
        
        # (start, end, increment)
        
        for i in range(0, n, 2):
            if s[i] != s[i+1]:
                count += 1
                
        return count
    
    
    #! Here is the Shortcut
    # return sum(s[i] != s[i+1] for i in range(0, len(s), 2))

        
sol = Solution()
print(sol.minChanges("11000111"))
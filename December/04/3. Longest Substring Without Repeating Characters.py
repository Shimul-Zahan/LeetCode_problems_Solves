
# * Unsolved

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        unique_set = set()
        for c in s:
            if c not in unique_set:
                unique_set.add(c)
                print(unique_set)
        return  len(unique_set)
            
    
sol = Solution()
print(sol.lengthOfLongestSubstring(s = "pwwkew"))
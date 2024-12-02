from collections import Counter

class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        count_s = Counter(s)
        count_t = Counter(t)
        result = count_t - count_s 
        return ''.join(result.keys())

sol = Solution()
print(sol.findTheDifference("aa", "aaa"))

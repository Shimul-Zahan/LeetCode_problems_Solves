class Solution(object):
    def maxUniqueSplit(self, s):
        def backtrack(start, set):
            if start == len(s):
                return 0
            max_splits = 0
            for i in range(start + 1, len(s) + 1):
                substring = s[start:i]
                if substring not in set:
                    set.add(substring)
                    max_splits = max(max_splits, 1 + backtrack(i, set))
                    set.remove(substring)        
            return max_splits
        return backtrack(0, set())
  
sol = Solution()
print(sol.maxUniqueSplit("aa"))


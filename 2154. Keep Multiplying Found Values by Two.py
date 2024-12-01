class Solution:
    def findFinalValue(self, nums, original):
        while original in nums:
            original *= 2
        return original
                
                
            
    
    
sol = Solution()
print(sol.findFinalValue([8,19,4,2,15,3], original=2))
  
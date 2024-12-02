class Solution:
    def missingNumber(self, nums):
        # ------sol 1----------
        n = len(nums)
        total = sum(nums)
        act_sum = n*(n+1) / 2
        
        # missing number gauss formula
        return int(act_sum - total)
    
        # ------sol 2----------
        # dict = {}
        # for num in nums:
        #     dict[num] = True
        
        # for i in range(len(nums)):
        #     if i not in dict:
        #         return i
        # return len(nums)
    
    
sol = Solution()
print(sol.missingNumber([0,1]))
class Solution(object):
    def find132pattern(self, nums):
        for i in range(len(nums) -1 ):
            if nums[i] <  nums[i+1]:
                return False
        return True 
sol = Solution()
print(sol.find132pattern([5,2,3,4]))
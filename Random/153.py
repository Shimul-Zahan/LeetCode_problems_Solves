class Solution(object):
    def findMin(self, nums):
        # target =  nums[0]
        # return nums[target]
        # return min(nums)
        min = nums[0]
        for i in range(1, len(nums)):
            if nums[i] < min:
                min = nums[i]
        return min

        
        
sol = Solution()
print(sol.findMin([11,13,15,17]))
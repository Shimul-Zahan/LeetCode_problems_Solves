class Solution(object):
    def removeDuplicates(self, nums):
        if len(nums) <= 2:
            return len(nums)
        
        i = 2
        for j in range(2 ,len(nums)):
            if nums[j] != nums[i - 2]:
                nums[i] == nums[j]
                i += 1
        return i
        
sol = Solution()
print(sol.removeDuplicates([0,0,1,1,1,1,2,3,3]))
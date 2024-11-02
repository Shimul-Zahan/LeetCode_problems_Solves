class Solution(object):
    def search(self, nums, target):
        for i in range(len(nums)):
            # print(nums[i], target)
            if nums[i] == target:
                return i
        return -1
        
sol = Solution()
print(sol.search([4,5,6,7,0,1,2], 11))
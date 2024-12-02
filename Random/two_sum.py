# O(n^2)
# class Solution(object):
#     def twoSum(self, nums, target):
#         for i in range(len(nums) - 1):
#             for j in range(i+1, len(nums)):
#                 if (nums[i] + nums[j]) == target:
#                     return [i, j]

# O(n)
class Solution(object):
    def twoSum(self, nums, target):
        dict = {}
        for i, num in enumerate(nums):
            result = target - num
            if result in dict:
                return [dict[result], i]
            dict[num] = i
        
s = Solution()
print(s.twoSum([3,2,3], 6))
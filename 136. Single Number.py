# class Solution:
#     def singleNumber(self, nums) -> int:
#         my_dict = {}
#         for i in range(len(nums)):
#             if nums[i] in my_dict:
#                 my_dict.pop(nums[i])
#             else:
#                 my_dict[nums[i]] = i
#         if len(my_dict) == 1:
#             return next(iter(my_dict))
#         else:
#             return None
        
# sol = Solution()
# print(sol.singleNumber([0,1,0,1,0,1,99]))


class Solution:
    def singleNumber(self, nums) -> int:
        ones, twos = 0, 0  # Initialize two variables to track bits
        for num in nums:
            # Update `ones` and `twos` to count bits
            ones = (ones ^ num) & ~twos
            twos = (twos ^ num) & ~ones
        return ones  # The unique number remains in `ones`

sol = Solution()
print(sol.singleNumber([0, 1, 0, 1, 0, 1, 99]))

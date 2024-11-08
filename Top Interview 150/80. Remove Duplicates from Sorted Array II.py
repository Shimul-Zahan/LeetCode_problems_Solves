class Solution(object):
    def removeDuplicates(self, nums):
        # dict = {}
        # count = 0
        # for num in nums:
        #     if num not in dict:
        #         dict[num] = []
        #     if len(dict[num]) < 2:
        #         dict[num].append(num)
        # # return [val for sublist in dict.values() for val in sublist ]
        
        # array = []
        
        # for sublist in dict.values():
        #     for val in sublist:
        #         array.append(val)
                
        # return len(array)
        
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
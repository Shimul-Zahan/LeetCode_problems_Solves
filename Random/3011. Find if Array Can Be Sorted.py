class Solution(object):
    def canSortArray(self, nums):
        if sorted(nums) == nums:
            return True
        dict = {}
        for num in nums:
            set_bit = bin(num).count('1')
            if set_bit not in dict:
                dict[set_bit] = []
            dict[set_bit].append(num)
        # return dict
        
        for key in dict:
            dict[key].sort()
        # return dict
        
        sorted_nums = []
        for num in nums:
            set_bit = bin(num).count('1')
            sorted_nums.append(dict[set_bit].pop(0))
            
        return sorted_nums == sorted(nums)
        
sol = Solution()
print(sol.canSortArray([75,34,30]))
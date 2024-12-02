class Solution:
    def singleNumber(self, nums) -> int:
        my_dict = {}
        for num in nums:
            if num in my_dict:
                my_dict[num] += 1
            else:
                my_dict[num] = 1
        # return my_dict
        
        for key, count in my_dict.items():
            if count == 1:
                return key

        

sol = Solution()
print(sol.singleNumber([0, 1, 0, 1, 0, 1, 99]))
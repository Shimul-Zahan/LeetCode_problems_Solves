class Solution:
    def singleNumber(self, nums) -> int:
        my_dict = {}
        for num in nums:
            if num in my_dict:
                my_dict[num] += 1
            else:
                my_dict[num] = 1
        # return my_dict
        
        updated_array = []
        
        for key, count in my_dict.items():
            # print(key, ":", count)
            if count == 1:
                updated_array.append(key)
        return updated_array

        

sol = Solution()
print(sol.singleNumber([1,2,1,3,2,5]))
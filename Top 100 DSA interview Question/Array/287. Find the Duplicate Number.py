class Solution(object):
    def findDuplicate(self, nums):
        # seen = set()
        # for num in nums:
        #     if num in seen:
        #         return num
        #     else:
        #         seen.add(num)
        # return None
        
        dict = {}
        count = 0
        for num in nums:
            if num in dict:
                return num
            dict[num] = True
        return None
                
                

                
sol = Solution()
print(sol.findDuplicate([1,3,4,2,2]))
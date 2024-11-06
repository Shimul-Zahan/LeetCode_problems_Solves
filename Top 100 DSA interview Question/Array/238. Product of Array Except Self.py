class Solution(object):
    def productExceptSelf(self, nums):
        new_array = []
        product = 1
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if j > len(nums):
                    j = 0
                product = product * nums[j]
            new_array.append(product)
            product = 1
            
        return new_array
        
            
        
sol = Solution()
print(sol.productExceptSelf([1,2,3,4]))
class Solution:
    def rotate(self, nums, k: int) -> None:
        n = len(nums)
        k = k % n
        nums.reverse()    
        nums[:k] = reversed(nums[:k]) 
        nums[k:] = reversed(nums[k:])
        return nums
        
        
sol = Solution()
print(sol.rotate(nums = [1,2,3,4,5,6,7], k = 3))
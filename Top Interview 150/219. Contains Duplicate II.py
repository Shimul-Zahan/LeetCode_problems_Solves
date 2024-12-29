class Solution:
    def containsNearbyDuplicate(self, nums, k: int) -> bool:
        dict = {}
        for i, num in enumerate(nums):
            if num in dict:
                if i - dict[num] <= k:
                    return True
            dict[num] = i
        return False
                
    
sol = Solution()    
print(sol.containsNearbyDuplicate(nums = [1,0,1,1], k = 1))

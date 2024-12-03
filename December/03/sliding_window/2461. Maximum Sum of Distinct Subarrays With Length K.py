class Solution:
    def maximumSubarraySum(self, nums, k: int) -> int:
        sum = 0
        maxSum = 0
        i = 0
        while(i<k):
            sum += nums[i]
            i+=1
        maxSum = sum
        # for loop for sliding
        for i in range(0, len(nums)-k+1):
            sum = (sum - nums[i-1]) + nums[i+k-1]
            maxSum = max(maxSum, sum)
        return maxSum
        

    
sol = Solution()
print(sol.maximumSubarraySum(nums = [1,5,4,2,9,9,9], k = 3))

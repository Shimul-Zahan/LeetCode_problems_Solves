class Solution:
    def majorityElement(self, nums) -> int:
        # sorted_array = sorted(nums)
        # return sorted_array[int(len(sorted_array) / 2)]
        
        # Boyer-Moore Voting Algorithm
        candidate, count = None, 0
        for num in nums:
            if count == 0:
                candidate = num
                print(candidate, 'candidate')
            count += (1 if num == candidate else -1)
            print(candidate, count, 'candidate', 'count')
            
        return candidate, count
                
        
sol = Solution()
print(sol.majorityElement(nums = [2,2,1,1,1,2,2]))
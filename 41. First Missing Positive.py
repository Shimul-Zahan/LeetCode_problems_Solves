class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        dict = {}
        for num in nums:
            dict[num] = True

        # smallest = min(nums)
        i = 1
        while True:
            if i not in dict:
                return i
            i+=1
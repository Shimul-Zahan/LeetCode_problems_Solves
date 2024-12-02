class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        array =  sorted(nums1 + nums2)
        print(array)
        if len(array) % 2 != 0:
            return array[len(array) // 2]
        else:
            mid = len(array) // 2
            return (array[mid-1] + array[mid]) / 2
sol = Solution()
print(sol.findMedianSortedArrays([1,3], [2,4]))
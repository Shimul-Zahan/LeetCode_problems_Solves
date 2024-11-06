class Solution(object):
    def merge(self, nums1, m, nums2, n):
        print(sorted(nums1[ 0:m ]+ nums2[ 0:n ]))
        
sol = Solution()
sol.merge(nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6,5], n = 3)

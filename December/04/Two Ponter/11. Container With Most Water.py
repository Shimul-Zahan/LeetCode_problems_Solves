class Solution:
    def maxArea(self, height) -> int:
        left, right = 0, len(height)-1
        max_area = 0
        # return min(height[left], height[right])
        while left < right:
            max_area = max(max_area, min(height[left], height[right] * (right - left)))
            
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
                
        return max_area
    
sol = Solution()
print(sol.maxArea(height = [1,8,6,2,5,4,8,3,7]))
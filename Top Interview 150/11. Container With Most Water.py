class Solution:
    def maxArea(self, height) -> int:
        first, last, area = 0, len(height) - 1, 0
        max_area = 0
        while first < last:
            area = min(height[first], height[last]) * (last - first)
            max_area = max (max_area, area)
            if height[first] < height[last]:
                first += 1
            else:
                last -= 1
        return max_area
    
sol = Solution()
print(sol.maxArea(height = [1,8,6,2,5,4,8,3,7]))
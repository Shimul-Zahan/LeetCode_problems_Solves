class Solution(object):
    def divide(self, dividend, divisor):
        result = int(dividend / divisor)
        return min(max(result, -2**31), 2**31 - 1)
    
sol = Solution()
print(sol.divide(-2147483648, -1))


#! ----------- Note ----------
class Solution:
    def maxProfit(self, prices) -> int:
        min_price = prices[0]
        max_profit = 0
        
        for price in prices:
            if price < min_price:
                min_price = price
            else:
                max_profit = max(max_profit, price - min_price)
        return max_profit
        
        
sol = Solution()
print(sol.maxProfit(prices = [7,1,5,3,6,4]))
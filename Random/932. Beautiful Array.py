class Solution:
    def beautifulArray(self, n: int):        
        # if n == 1:
        #     return [1]
        
        # odd_part = self.beautifulArray((n+1) // 2)
        # even_part = self.beautifulArray( n // 2)
        
        # result = [2 * x - 1 for x in odd_part] + [2 * x for x in even_part]
        
        # return result
        
        #! -------- second sol ---------
        result = [1]
        
        while len(result) < n:
            odd = [ 2 * i - 1 for i in result]
            even = [ 2 * i for i in result]
            result = odd + even
        return [i for i in result if i <= n]
        
         
    
    
sol = Solution()
print(sol.beautifulArray(5))
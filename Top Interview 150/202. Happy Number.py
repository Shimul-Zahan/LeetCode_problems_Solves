class Solution():
    def isHappy(self, n):
        sum_of_squares = set()
        while n !=1:
            
            if n in sum_of_squares:
                return False
            
            sum_of_squares.add(n)
            
            digits = [int(digit) for digit in str(n)]
            n = sum(digit ** 2 for digit in digits)
                    
        return True
            
    
sol  = Solution()
print(sol.isHappy(n=19))
# class Solution:
#     def countPrimes(self, n: int) -> int:
#         if n <= 1:
#             return False
#         if n <= 3:
#             return True
#         if n % 2 == 0 or n % 3 == 0:
#             return False
#         for i in range(5, int(math.sqrt(n)) + 1, 6):
#             if n % i == 0 or n % (i + 2) == 0:
#                 return False
#         return True
        
#     return sum(1 for i in range(2, N + 1) if is_prime(i))
    
    
# sol = Solution()
# print(sol.countPrimes(10))
class Solution:
    def addToArrayForm(self, num, k: int):
        sum = int(''.join(map(str, num))) + k
        return list(map(int, str(sum)))
    
    
sol = Solution()
print(sol.addToArrayForm(num = [1,2,0,0], k = 34))
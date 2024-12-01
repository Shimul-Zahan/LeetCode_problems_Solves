class Solution:
    def checkIfExist(self, arr):
        exist = set()
        
        for num in arr:
            if num*2 in exist or num/2 in exist:
                return True
            
            exist.add(num)
        return False
            
    
    
sol = Solution()
print(sol.checkIfExist([10,2,5,3]))
  
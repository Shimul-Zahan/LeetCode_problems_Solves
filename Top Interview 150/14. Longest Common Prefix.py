class Solution:
    def longestCommonPrefix(self, strs) -> str:
        lgp = strs[0]
        
        for str in strs[1:]:
            while not str.startswith(lgp):
                lgp = lgp[:-1]
                if not lgp:
                    return ""
                
        return lgp
            
    
sol=Solution()
print(sol.longestCommonPrefix(strs = ["flower","flow","flight"]))
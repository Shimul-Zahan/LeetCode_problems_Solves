class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        n= len(s)
        s_t = {}
        t_s = {}
        
        for i in range(n):
            if s[i] in s_t:
                if s_t[s[i]] != t[i]:
                    return False
            else:
                s_t[s[i]] = t[i]
                print(s_t)
            
            if t[i] in t_s:
                if t_s[t[i]] != s[i]:
                    return False
            else:
                t_s[t[i]] = s[i]
        return True
        
sol = Solution()
print(sol.isIsomorphic(s = "egg", t = "add"))

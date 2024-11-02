class Solution(object):
    def makeFancyString(self, s):
        
        fancy_array = []
        
        for i in s:
            if len(fancy_array) >= 2 and fancy_array[-1] == i and fancy_array[-2] == i:
                continue
            fancy_array.append(i)
        return ''.join(fancy_array)
                
        
        
Sol = Solution()
print(Sol.makeFancyString('aaabaaaa'))
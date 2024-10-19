class Solution(object):
    def findKthBit(self, n, k):
        
        string = "0"
        reverse_table = str.maketrans('01', '10')
        
        if n > 1:
            for i in range(1, n):
                string = string + "1" + ''.join(reversed(string)).translate(reverse_table)
            if  1 <= k <= len(string):
                return string[k-1]
        else:
            return '"0"'
        
sol = Solution()
print(sol.findKthBit(1, 1))
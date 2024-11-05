class Solution(object):
    def compress(self, chars, k):
        
        n = len(chars)
        count = 1
        ch = chars[0]
        new_array = []
        
        if n == 0:
            return 0
        
        for i in range(1, n):
            if chars[i] == ch:
                count += 1
            else:
                new_array.append(ch)
                if count > 1:
                    new_array.append(str(count))
                ch = chars[i]
                count = 1
        new_array.append(ch)
        if count > 1:
            new_array.append(str(count))
        return len(''.join(new_array)) - k
        
        
sol = Solution()
print(sol.compress("aabaabbcbbbaccc", 6))
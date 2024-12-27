class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        length_of_needle = len(needle)
        length_of_haystack = len(haystack)
        
        for i in range(length_of_haystack - length_of_needle + 1):
            if haystack[i: i+length_of_needle] == needle:
                return i
        return -1

sol = Solution()
print(sol.strStr(haystack = "sadbutsad", needle = "sad"))
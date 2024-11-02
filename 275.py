class Solution(object):
    def hIndex(self, citations):
        l = len(citations)
        print(l/2)
        print(sum(citations))
        if l > 2:
            return citations[l//2]
        if l <= 2 and sum(citations) == 0:
            return 0
        return 1
sol = Solution()
print(sol.hIndex([0,0]))
class Solution(object):
    def rotateString(self, s, goal):
        return goal in (s+s) and len(s) == len(goal)

sol = Solution()
print(sol.rotateString("aa", "a"))      
class Solution:
    def addSpaces(self, s: str, spaces):
        # # ! Convert this string to an array
        # s_list = list(s)
        # for index, space in enumerate(spaces):
        #     # ! In an array we can insert/delete item in any index
        #     s_list.insert(space+index, " ")
        # return ''.join(s_list)
        
        result = []
        space_set = set(spaces)
        for i, c in enumerate(s):
            if i in space_set:
                result.append(" ")
            result.append(c)
        return "".join(result)
    
sol = Solution()
print(sol.addSpaces(s = "LeetcodeHelpsMeLearn", spaces = [8,13,15]))
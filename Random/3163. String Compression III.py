# class Solution(object):
#     def compressedString(self, word):
        
#         #! --------- dictionary work must need to know --------
#         # count = {}
        
#         # for letter in word:
#         #     count[letter] = count.get(letter, 0) + 1
        
#         # # print(count.items())
        
#         result = []
#         count = 1 
#         n = len(word)
#         char = word[0]
        
#         for i in range(1, n):
#             if word[i] == char and count < 9:
#                 count += 1
#             else:
#                 result.append(f"{count}{char}")
#                 char = word[i]
#                 count = 1
#         result.append(f"{count}{word[-1]}")
#         return ''.join(result)
        
        
# sol = Solution()
# print(sol.compressedString('abdec'))

class Solution(object):
    def compressedString(self, word):
        array = []
        count = 1
        n = len(word)
        ch = word[0]
        
        for i in range(1, n):
            if word[i] == ch and count < 9:
                count += 1
            else:
                array.append(str(count))
                array.append(ch)
                ch = word[i]
                count = 1
        array.append(str(count))
        array.append(ch)
        return ''.join(array)
        
sol = Solution()
print(sol.compressedString('bbbbbbbbbbbbbbbbbbr'))
class Solution:
    def groupAnagrams(self, strs):
        my_dict = {}
        
        for word in strs:
            char_array = list(word)
            char_array.sort()
            sort_word = ''.join(char_array)
            print(sort_word)
            if sort_word not in my_dict:
                my_dict[sort_word] = []
            my_dict[sort_word].append(word)
        return list(my_dict.values())
    
    
sol = Solution()
print(sol.groupAnagrams(strs = ["eat","tea","tan","ate","nat","bat"]))
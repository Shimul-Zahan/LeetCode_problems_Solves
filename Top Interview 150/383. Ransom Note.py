class Solution:
    def canConstruct(self, ransomNote: str, magazine: str):
        dict = {}
        for note in magazine:
            dict[note] = dict.get(note, 0) + 1
        
        for note in ransomNote:
            if dict.get(note, 0) == 0:
                return False
            dict[note] -= 1
        return True
        
    
sol = Solution()
print(sol.canConstruct(ransomNote = "a", magazine = "b"))
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split()

        char_to_word = {}  # Map for character to word
        word_to_char = {}  # Map for word to character

        for char, word in zip(pattern, words):
            # Check and map character to word
            if char in char_to_word:
                if char_to_word[char] != word:  # Conflict in mapping
                    return False
            else:
                char_to_word[char] = word
            
            # Check and map word to character
            if word in word_to_char:
                if word_to_char[word] != char:  # Conflict in mapping
                    return False
            else:
                word_to_char[word] = char

        return True

sol = Solution()
print(sol.wordPattern(pattern = "abba", s = "dog cat cat dog"))
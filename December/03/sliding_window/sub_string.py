# সর্বোচ্চ দৈর্ঘ্যের ইউনিক সাবস্ট্রিং খুঁজুন।
def longest_unique_substring(s):
    start = 0
    char_set = set()
    max_length = 0
    
    for end in range(len(s)):
        while s[end] in char_set:  # পুনরাবৃত্তি ঘটলে
            char_set.remove(s[start])
            start += 1
        char_set.add(s[end])
        max_length = max(max_length, end - start + 1)
    
    return max_length

# উদাহরণ
print(longest_unique_substring("abcabcbb"))  # Output: 3 (abc)

# k অপারেশন ব্যবহার করে সর্বাধিক পুনরাবৃত্তি বের করা
def character_replacement(s, k):
    count = {}
    max_count = 0
    start = 0
    
    for end in range(len(s)):
        count[s[end]] = count.get(s[end], 0) + 1
        max_count = max(max_count, count[s[end]])
        
        while (end - start + 1) - max_count > k:  # k সীমা অতিক্রম করলে
            count[s[start]] -= 1
            start += 1
    
    return end - start + 1

# উদাহরণ
print(character_replacement("AABABBA", 1))  # Output: 4

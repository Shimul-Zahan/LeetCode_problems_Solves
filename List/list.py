def definition():
    """
    লিস্ট হচ্ছে একটি মিউটেবল ডাটা স্ট্রাকচার যা সিকোয়েন্স ভ্যালু ধারন করে। এটি এরে এর মতো হলেও এর সাইজ পরিবর্তনশীল।
অপারেশন:
ইনসার্ট, ডিলিট, অ্যাক্সেস সব অপারেশন গুলি O(n) সময় নিতে পারে, কারণ এলিমেন্টগুলির মধ্যে সরানো বা ইনসার্ট করার জন্য অনেকে শিফট করতে হয়।
    """
    
    lst = [1, 2, 3, 4]
    print(f"Full list here {lst}")
    lst.append(5)
    print(f"New append item {lst}")
    lst.remove(4)
    print(f"removed list {lst}")
    lst.pop(0)  # remove item in index = 0
    print(f"popped by index {lst}")
    del lst[1]   # delete item at index 1
    print(f"delted list {lst}")
    return lst
    

# print("add new item in array", definition())
print("remove item in array", definition())
    
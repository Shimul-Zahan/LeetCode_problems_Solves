# variable size sliding window
def min_length_subarray(arr, target):
    # ইনিশিয়াল ভেরিয়েবল
    start = 0  # উইন্ডোর শুরু পয়েন্ট
    window_sum = 0  # বর্তমান উইন্ডোর যোগফল
    min_length = float('inf')  # সর্বনিম্ন দৈর্ঘ্যের জন্য

    # উইন্ডোর শেষ পয়েন্ট
    for end in range(len(arr)):
        window_sum += arr[end]  # নতুন এলিমেন্ট যোগ
        
        # যতক্ষণ যোগফল ≥ টার্গেট
        while window_sum >= target:
            # সর্বনিম্ন দৈর্ঘ্য আপডেট
            min_length = min(min_length, end - start + 1)
            # উইন্ডোর প্রথম এলিমেন্ট বাদ
            window_sum -= arr[start]
            start += 1  # উইন্ডোর শুরু পয়েন্ট এগিয়ে নিয়ে যান

    # ফলাফল রিটার্ন
    return min_length if min_length != float('inf') else 0


print(min_length_subarray(arr = [2, 3, 1, 2, 4, 3], target = 7))
class Solution:
    def slidingWindow(self, arr, k):
        sum = 0
        maxSum = 0
        i=0
        while(i < k):
            sum += arr[i]
            i += 1
        maxSum = sum
        
        for i in range(1, len(arr) - k + 1):
            prevSum = arr[i - 1]
            nextSum = arr[i+k -1]
            sum = sum - prevSum + nextSum
            maxSum = max(maxSum, sum)
        return maxSum 
        

    
sol = Solution()
print(sol.slidingWindow([100, 200, 300, 400], k=2))


class Solution:
    def slidingWindow(self, arr, k):
        # প্রথম উইন্ডোর যোগফল বের করা
        window_sum = sum(arr[:k])
        max_sum = window_sum
        
        # সর্বোচ্চ যোগফল সাবঅ্যারের ইন্ডেক্সের জন্য
        start_index = 0
        
        # স্লাইডিং উইন্ডো
        for i in range(1, len(arr) - k + 1):
            # উইন্ডোর নতুন মান আপডেট
            window_sum = window_sum - arr[i - 1] + arr[i + k - 1]
            
            # সর্বোচ্চ যোগফল আপডেট এবং ইন্ডেক্স সংরক্ষণ
            if window_sum > max_sum:
                max_sum = window_sum
                start_index = i  # নতুন উইন্ডোর শুরু ইন্ডেক্স
        
        # শেষ ইন্ডেক্স = শুরু ইন্ডেক্স + উইন্ডোর আকার - 1
        end_index = start_index + k - 1
        
        return max_sum, (start_index, end_index)

# উদাহরণ
sol = Solution()
max_sum, indices = sol.slidingWindow([100, 200, 300, 400], k=2)
print("Max Sum:", max_sum)          # Output: 700
print("Indices:", indices)          # Output: (2, 3)

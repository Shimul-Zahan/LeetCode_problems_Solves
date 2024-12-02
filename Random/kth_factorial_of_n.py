class Solution(object):
    def kthFactor(self, n, k):
        array = []
        for i in range(1, n+1):
            if n % i == 0:
                array.append(i)
        if k <= len(array):
            for index in range(0, len(array)):
                if index == k - 1:
                    return array[index]
        else: return -1
        
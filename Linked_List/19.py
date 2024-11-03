# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        length = 0
        temp = head
        while temp:
            length += 1
            temp = temp.next

        # if n < 0 or n >= length:
        #     return head.next

        if n == length:
            return head.next
        
        temp = head
        n = length - n
        for _ in range(n - 1):
            temp = temp.next
        remove_node = temp.next
        temp.next = remove_node.next
        return head
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteMiddle(self, head):

        if not head or not head.next:
            return None
            
        length = 0
        temp = head
        while temp:
            length += 1
            temp = temp.next
        
        temp = head
        target = length // 2

        for _ in range(target - 1):
            temp = temp.next
        delete_node = temp.next
        temp.next = delete_node.next
        delete_node.next = None
        return head

        
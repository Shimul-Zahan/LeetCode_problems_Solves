# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        current = dummy
        while head:
            if head.next:
                current.next = ListNode(head.next.val)
                current = current.next
            current.next = ListNode(head.val)
            head = head.next.next
        